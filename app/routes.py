from app import app
from flask import render_template,redirect,abort
from app.db import Database
from app.bitcoin import Bitcoin
from flask import request
from app import configuration
#from app.bitcoin import Bitcoin
import re
import hashlib


@app.route('/')
def index():
    database=Database()
    bitcoin=Bitcoin()
    database.db_cursor.execute('SELECT * FROM items WHERE visible!=0')
    items = database.db_cursor.fetchall()
    return render_template('base.html', items=items, rate=bitcoin.btc_eur, header=configuration.Configuration.header)

@app.route('/item/<index>')
def show_item(index):
    index=re.sub('[^0-9]', '', index)
    database=Database()
    bitcoin=Bitcoin()
    item1=database.fetch_one_item(index)

    if item1 is None:
        return 'Error'
    else:
        return  render_template('item.html',index=index,item=item1,rate=bitcoin.btc_eur,header=configuration.Configuration.header)
@app.route('/order/<index>/<amount>')
def order_item(index,amount):
    index=re.sub('[^0-9]', '', index)
    amount=re.sub('[^0-9]', '', amount)
    database=Database()
    bitcoin=Bitcoin()
    item1=database.fetch_one_item(index)
    if item1 is None:
        return 'Error'
    else:
        from flask_wtf import FlaskForm
        from wtforms import TextAreaField,validators
        class OrderForm(FlaskForm):
            address=TextAreaField('Address', [validators.Length(min=10, max=200)])
        order_form=OrderForm()
        return render_template('order.html',item=item1, index=index,rate=bitcoin.btc_eur, amount=int(amount),form=order_form,header=configuration.Configuration.header)
@app.route('/payment', methods=['POST'])
def pay_for_order ():
    data=request.form
    address=data['address']
    address=address[0:200]
    address=address.strip()
    if address=="":
        return "Error, empty address"
    bitcoin=Bitcoin()
    database=Database()
    #address=re.sub('[^A-Za-z0-9:_-]','',address)
    address_salt=address+configuration.Configuration.salt
    address_salt=address_salt.encode()
    address_hash=hashlib.sha224(address_salt).hexdigest()[0:9]
    address=address.replace('\n', '|')
    address = re.sub('[^A-Za-z0-9:_-|]', '', address)
    item_index=data['index']
    item_amount=data['amount']
    item_index=re.sub('[^0-9]', '', item_index)
    item_amount=re.sub('[^0-9]', '', item_amount)
    item1=database.fetch_one_item(item_index)
    order_price=round(item1.price/bitcoin.btc_eur*float(item_amount),6)
    #print (order_price)
    order=Bitcoin.order(item_index,address,address_hash,item_amount,order_price)
    #print (order.order_index)
    return redirect("/pay/"+str(order.btc_address))
@app.route('/pay/<btc_address>')
def present_payment(btc_address):
    btc_address=re.sub('[^A-Za-z0-9]','',btc_address)
    bitcoin=Bitcoin()
    database=Database()
    order=database.fetch_one_order(btc_address)
    if order is None:
        return 'Error'
    else:
        return  render_template('pay.html',order=order,rate=bitcoin.btc_eur,header=configuration.Configuration.header)
@app.route('/o/<key1>/<key2>')
def list_paid_orders(key1,key2):
    if key1==configuration.Configuration.adminkey1:
        if key2==configuration.Configuration.adminkey2:
            database=Database()
            orders2=database.get_orders(0)
            orders=[]
            for order in orders2:
                if order.paid!=0:
                    orders.append(order)
            return render_template('admin-orders.html',header=configuration.Configuration.header,orders=orders)
    abort(404)
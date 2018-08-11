import sqlite3
from app import configuration
class Database:
    class order: #information about order
        index=0
        address=''
        wif=''
        private_key=''
        paid=0
        address_salt=''
        item_index=0
        item_amount=0
        btc_address=''
        order_price=0
        order_date=0
        item_name=''
        pcs=[]
        def __init__(self,row):
            self.index=row[0]
            self.address=row[1]
            self.wif=row[2]
            self.private_key=row[3]
            self.paid=row[4]
            self.address_salt=row[5]
            self.item_index=row[6]
            self.item_amount=row[7]
            self.btc_address=row[8]
            self.order_price=row[9]
            self.order_date=row[10]
            self.note=row[11]
            self.item_name=''

    class row: #item row
        name=''
        index=-1
        price=''
        avail=''
        desc=''
        pcs=[]
        def __init__(self,row):
            self.name=row[0]
            self.index=row[1]
            self.price=row[2]
            self.avail=row[3]
            self.desc=row[4]
            self.pcs = [int(pc) for pc in row[5].split(',')]


    def __init__(self): #init database
        self.db_connection= sqlite3.connect(configuration.Configuration.database_url)
        self.db_cursor=self.db_connection.cursor()

    def update_btc_rate(self,rate):
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute('UPDATE btc SET rate='+str(rate)+'  WHERE rate >0')
        self.db_connection.commit()

    def create_note(self,order_index,note):
        self.db_connection.set_trace_callback(print)
        self.db_cursor.execute('UPDATE orders SET `note`="'+note+'"  WHERE `index`='+order_index)
        self.db_connection.commit()
    def delete_note(self,order_index):
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute('UPDATE orders SET `note`=null  WHERE `index`='+order_index)
        self.db_connection.commit()

    def update_paid(self,btc_address,cash):
        #print (btc_address+' '+str(cash))
        self.db_cursor.execute('UPDATE orders SET paid='+str(cash)+' WHERE btc_address="'+btc_address+'"')
        self.db_connection.commit()

    def get_orders(self,cut_off):
        self.db_cursor.execute('SELECT * FROM orders WHERE date>'+str(cut_off))
        orders=[]
        for order_row in self.db_cursor.fetchall():
            orders.append(self.order(order_row))
        return orders
    def get_items(self):
        self.db_cursor.execute('SELECT * FROM items')
        items=[]
        for item_row in self.db_cursor.fetchall():
            items.append(self.row(item_row))
        return items


    def fetch_one_order(self,btc_address): #return one order in form of ''order'' class
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute('SELECT * FROM orders where btc_address="'+str(btc_address)+'"')
        order=self.db_cursor.fetchone()
        if order is None:
            return None
        else:
            return self.order(order)
    def fetch_one_item(self,index): #return one '''row''' item from items
        self.db_cursor.execute('SELECT * FROM items WHERE ind=' + str(index))
        item=self.db_cursor.fetchone()
        if item is None:
            return None
        else:
            return_row=self.row(item)
            return return_row
    def make_order(self,item_index,address,address_salt,item_amount,order_price): #pairedd with update_order, making new order
        import time
        self.db_cursor.execute("""INSERT INTO `orders`(`item_index`, `address`,  `address_salt`,`item_amount`,`order_price`,`paid`,`date`)        VALUES(?,?,?,?,?,0,?)""",(item_index,address,address_salt,item_amount,order_price,int(time.time())));
        self.db_connection.commit()
        return self.db_cursor.lastrowid
    def update_order(self,order_index,wif_key,btc_address,private_key): #paired with make_order, making new order
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute("UPDATE orders SET wif=?,  private_key=?, btc_address=? WHERE `index`=?;",(wif_key,private_key,btc_address,order_index))
        self.db_connection.commit()
    def update_item(self,item_index,item_price,item_name,item_avail,item_desc,item_pcs):
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute("UPDATE items SET name=?,  price=?, visible=?, description=?, pcs=? WHERE `ind`=?;", (item_name, item_price, item_avail,item_desc,item_pcs,  item_index))
        self.db_connection.commit()
    def delete_item(self,item_index):
        self.db_cursor.execute("DELETE FROM `items` WHERE `ind`="+item_index)
        self.db_connection.commit()
    def add_item(self):
        self.db_cursor.execute("INSERT INTO `items`(`name`,`price`,`visible`,`description`,`pcs`) VALUES ('Empty item','0',0,'Change description and visibility','1,2,3,4,5');")
        self.db_connection.commit()
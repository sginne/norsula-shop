import sqlite3
from app import configuration
class Database:
    class order:
        index=0
        address=''
        wif=''
        private_key=''
        paid=0
        address_salt=''
        item_index=0
        item_ammount=0
        btc_address=''
        order_price=0

    class row:
        name=''
        price=''
        avail=''
        desc=''
    def __init__(self):
        self.db_connection= sqlite3.connect(configuration.Configuration.database_url)
        self.db_cursor=self.db_connection.cursor()
    def fetch_one_order(self,btc_address):
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute('SELECT * FROM orders where btc_address="'+str(btc_address)+'"')
        order=self.db_cursor.fetchone()
        if order is None:
            return None
        else:
            return_order=self.order()
            return_order.index=order[0]
            return_order.address=order[1]
            return_order.wif=order[2]
            return_order.private_key=order[3]
            return_order.paid=order[4]
            return_order.address_salt=order[5]
            return_order.item_index=order[6]
            return_order.item_ammount=order[7]
            return_order.btc_address=order[8]
            return_order.order_price=order[9]
            return return_order
    def fetch_one_item(self,index):
        self.db_cursor.execute('SELECT * FROM items WHERE ind=' + str(index))
        item=self.db_cursor.fetchone()
        if item is None:
            return None
        else:
            return_row=self.row()
            return_row.name = item[0]
            return_row.price = item[2]
            return_row.avail = item[3]
            return_row.desc = item[4]
            return return_row
    def make_order(self,item_index,address,address_salt,item_amount,order_price):
        self.db_cursor.execute("""INSERT INTO `orders`(`item_index`, `address`,  `address_salt`,`item_amount`,`order_price`,`paid`)        VALUES(?,?,?,?,?,0)""",(item_index,address,address_salt,item_amount,order_price));
        self.db_connection.commit()
        return self.db_cursor.lastrowid
    def update_order(self,order_index,wif_key,btc_address,private_key):
        #self.db_connection.set_trace_callback(print)
        self.db_cursor.execute("UPDATE orders SET wif=?,  private_key=?, btc_address=? WHERE `index`=?;",(wif_key,private_key,btc_address,order_index))
        self.db_connection.commit()
    def read_order(self,order_index):
        self.db_connection.execute()

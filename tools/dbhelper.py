
def store_signal(stock_code, tuplelist, cursor):
    # insert_qry = "INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,? ,? ,? ,?);", tuplelist
    # cursor.execute(insert_qry)
    tablename = "signals_"+stock_code
    cursor.execute("INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,? ,? ,? ,?);", tuplelist)

def store_order(stock_code, tuplelist, cursor):
    # insert_qry = "INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,? ,? ,? ,?);", tuplelist
    # cursor.execute(insert_qry)
    tablename = "orderbook_"+stock_code
    cursor.execute("INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,?);", tuplelist)

def createsignaltable(stock_code, cursor):
    # ['Date','Time','Open','High','Low','Close','Signal','Price','alpha']
    create_qry = "create table if not exists {}(Date TEXT,Time TEXT,Open REAL,High REAL,Low REAL,Close REAL,Signal CHARACTER(1),Price REAL,alpha REAL);".format("signals_"+stock_code)
    cursor.execute(create_qry)

def createordertable(stock_code, cursor):
    # ['Symbol','Date','Time','Order','Qty','Price']
    create_qry = "create table if not exists {}(Symbol VARCHAR(15),Date TEXT,Time TEXT,Order CHAR(1),Qty INT,Price REAL);".format("orderbook_"+stock_code)
    cursor.execute(create_qry)


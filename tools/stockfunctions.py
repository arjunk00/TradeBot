from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from nsetools import Nse
from nsepy import get_history
from datetime import date
import csv
import math
import datetime
import pandas as pd
import psycopg2

nse = Nse()


def fallbuy(stock_code):
    data = get_history(symbol=stock_code, start=date(2019, 1, 1), end=date(2020, 1, 1))['Close']
    prevavg = data.mean()
    datacov = get_history(symbol=stock_code, start=date(2020, 3, 1), end=date(2021, 3, 1))['Close']
    covavg = datacov.mean()
    expectedreturn = (prevavg - covavg) * 100 / covavg
    fallperc = (prevavg - covavg) * 100 / prevavg
    q = nse.get_quote(stock_code)['lastPrice']
    if q < prevavg:
        return (stock_code, True, expectedreturn, fallperc, prevavg, covavg, prevavg - covavg)
    else:
        return (stock_code, False, expectedreturn, fallperc, prevavg, covavg, prevavg - covavg)


def yearlyreturn(profit_percent, time):
    t = time.total_seconds()
    k = datetime.timedelta(365).total_seconds()
    return (((1 + (profit_percent / 100)) ** (k / t)) - 1) * 100


def marubozu(stock_code, day):
    data = get_history(symbol=stock_code, start=day, end=day)
    # print(data)
    open, close, high, low = data['Open'].values, data['Close'].values, data['High'].values, data['Low'].values
    # print(open)
    if open.size == 0:
        return {'stock_code': stock_code, 'date': day, 'trading_day': False, 'marubozu': None, 'bull': None}
    else:
        open, close, high, low = data['Open'].values[0], data['Close'].values[0], data['High'].values[0], \
                                 data['Low'].values[0]
        if open == low and close == high:
            return {'stock_code': stock_code, 'date': day, 'trading_day': True, 'marubozu': True, 'bull': True}
        elif open == high and close == low:
            return {'stock_code': stock_code, 'date': day, 'trading_day': True, 'marubozu': True, 'bull': False}
        else:
            return {'stock_code': stock_code, 'date': day, 'trading_day': True, 'marubozu': False, 'bull': None}


def stock_code_to_token(tradingsymbol):
    ts = tradingsymbol
    conn = psycopg2.connect(database="marubozu_data", user="admin", password="xtremebutter", host="192.168.1.25",
                            port="5432")
    cur = conn.cursor()
    fetch_token = "SELECT instrument_token from nse_tokens WHERE tradingsymbol='{}';".format(ts)
    cur.execute(fetch_token)
    tokens = cur.fetchall()[0]
    conn.close()
    return tokens[0]


def token_to_stock_code(token):
    conn = psycopg2.connect(database="marubozu_data", user="admin", password="xtremebutter", host="192.168.1.25",
                            port="5432")
    cur = conn.cursor()
    fetch_token = "SELECT tradingsymbol from nse_tokens WHERE instrument_token='{}';".format(str(token))
    cur.execute(fetch_token)
    stock_codes = cur.fetchall()[0]
    conn.close()
    return stock_codes[0]


def ohlc(ticks):
    open = ticks[0]
    close = ticks[-1]
    ticks.sort()
    low = ticks[0]
    high = ticks[-1]
    return [open, high, low, close]


def store(tablename, tuplelist, cursor):
    # insert_qry = "INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,? ,? ,? ,?);", tuplelist
    # cursor.execute(insert_qry)
    cursor.execute("INSERT INTO "+str(tablename)+" values (? ,? ,? ,? ,? ,? ,? ,? ,?);", tuplelist)



def createsignaltable(stock_code, cursor):
    # ['Date','Time','Open','High','Low','Close','Signal','Price','alpha']
    create_qry = "create table if not exists {}(Date TEXT,Time TEXT,Open REAL,High REAL,Low REAL,Close REAL,Signal CHARACTER(1),Price REAL,alpha REAL);".format(
        stock_code)
    cursor.execute(create_qry)


def converger(listofrows): #converge n DOHLCV rows into one
    D = listofrows[0][0]
    O = listofrows[0][1]
    C = listofrows[-1][-2]
    Lh = []
    Ll = []
    V = 0
    for row in listofrows:
        Lh.append(float(row[2]))
        Ll.append(float(row[3]))
        V += float(row[-1])
    H = max(Lh)
    L = min(Ll)

    return [D,O,H,L,C,V]

# print(yearlyreturn(15,datetime.timedelta(days=90)))

# day = datetime.date(2021,12,30)
# print(marubozu('infy',day))
# print(M)
# data = get_history(symbol='infy',start=day,end=day)
# # print(data)

import sys
sys.path.insert(0,"../kite_files")
from kiteconnect_trade import *
from pickleextract import *
from tools.stockfunctions import stock_code_to_token, token_to_stock_code, ohlc, store, createsignaltable
import datetime as dt
# you need following packages
import numpy as np
import pandas as pd
import sklearn
import sqlite3
import os
import statistics as stat
import math
import pickle
# some might be useless depending on operations but nothing outside of this is required
conn = sqlite3.connect("../databases/ticker_fw_test.db")
cursor = conn.cursor()
last_Nmin = []
delt = dt.timedelta(minutes=1)
last_Nmincopy = []
stock_code = 'ADANIPORTS'
createsignaltable(stock_code, cursor)


def on_ticks(ws, ticks):
    for tick in ticks:
        if len(last_Nmin) == 0:
            last_Nmin.append(dt.datetime.now())
            last_Nmin.append(tick['last_price'])
        elif dt.datetime.now() <= last_Nmin[0] + delt:
            last_Nmin.append(tick['last_price'])
        elif dt.datetime.now() > last_Nmin[0] + delt:
            last_Nmincopy = last_Nmin
            last_Nmincopy.append(tick['volume'])
            last_Nmin = []


def on_connect(ws, response):
    token = stock_code_to_token(stock_code)
    ws.subscribe([token])

    ws.set_mode(ws.MODE_LTP, [token])


def on_close(ws, code, reason):
    ws.stop()


threshold_dict = {'DRREDDY': 0.41878420750591105, 'HINDUNILVR': 0.43559159507797407,
                  'ADANIPORTS': 0.6452825406318907, 'AXISBANK': 0.4541107217201816}

while True:
    if last_Nmincopy[0] + delt <= dt.datetime.now() < last_Nmincopy[0] + 2 * delt:
        # this is input at each time stamp (at the end of time)
        # df = ['Open', 'High','Low','Close','Volume']
        df = ohlc(last_Nmincopy[1:-1])
        df.append(last_Nmincopy[-1])
        linregobj = regobj(stock_code)
        up_prob = linregobj.predict(df)  # denoted as alpha in pdf
        if up_prob > threshold_dict[stock_code]:
            if df[0] > df[3]:
                print("B")
                signal = "B"
                ltp = last_Nmin[-1]
                date_time = dt.datetime.now()

            else:
                print("H")
                signal = None
                ltp = last_Nmin[-1]
                date_time = dt.datetime.now()
        else:
            if df[0] > df[3]:
                print("H")
                signal = None
                ltp = last_Nmin[-1]
                date_time = dt.datetime.now()
            else:
                print("S")
                signal = "S"
                ltp = last_Nmin[-1]
                date_time = dt.datetime.now()
        tuplelist = (str(date_time.date()), str(date_time.time()), df[0], df[1], df[2], df[3], signal, ltp, up_prob)
        store(stock_code, tuplelist, cursor)
        conn.commit()
        last_Nmincopy = []

    else:
        print("You shouldnt be here")

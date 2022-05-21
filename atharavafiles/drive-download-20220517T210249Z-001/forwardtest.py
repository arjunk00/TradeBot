from kiteconnect_trade import *
from stockfunctions import stock_code_to_token, token_to_stock_code, ohlc
import datetime as dt
# you need following packages
import numpy as np
import pandas as pd
import sklearn

import os
import statistics as stat
import math
import pickle

# some might be useless depending on operations but nothing outside of this is required
last_Nmin = []
delt = dt.timedelta(minutes = 5)
last_Nmincopy = []
def on_ticks(ws,ticks):
    for tick in ticks:
        if len(last_Nmin) == 0:
            last_Nmin.append(dt.datetime.now())
            last_Nmin.append(tick['last_price'])
        elif dt.datetime.now() <= last_Nmin[0] + delt:
            last_Nmin.append(tick['last_price'])
        elif dt.datetime.now() > last_Nmin[0] +delt:
            last_Nmincopy = last_Nmin
            last_Nmin = []

def on_connect(ws, response):
    token = stock_code_to_token('ADANIPORTS')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_LTP, [token])


def on_close(ws, code, reason):
    ws.stop()


while True:
    if last_Nmincopy[0] + delt <= dt.datetime.now() < last_Nmincopy[0] + 2*delt:
        df = ohlc(last_Nmincopy[1:])


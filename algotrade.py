import logging
# from kitedata_postgres import *
from kiteconnect import KiteTicker
# from stockfunctions import stock_code_to_token, token_to_stock_code
from kiteconnect_trade import *
import statistics as st
import csv
import time

# logging.basicConfig(level=logging.DEBUG)
# api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
# api_key = "t44a8jbiydzpqq8b"
# access_token = "dofi017V4RNn7VBe1RPH22oeKf3elDdI"
kws = KiteTicker(api_key, access_token)


last_100 = []

def on_ticks(ws, ticks):
    for tick in ticks:
        if len(last_100)<=100:
            last_100.append(tick['last_price'])
        else:
            del last_100[0]
            last_100.append(tick['last_price'])




def on_connect(ws, response):
    token = 3677697 #stock_code_to_token('IDEA')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_LTP,[token])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect(threaded=True)

while True:
    if last_100<99:
        continue
    else:
        mode = st.mode(last_100)
        print(mode)



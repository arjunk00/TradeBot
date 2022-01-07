import logging
# from kitedata_postgres import *
from kiteconnect import KiteTicker
# from stockfunctions import stock_code_to_token, token_to_stock_code
from kiteconnect_trade import *
from access_token import *
# from kite_settings import *
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
bought = True
sold = True
buy_id = ''
sell_id = ''
while True:
    if len(last_100)<99:
        continue
    else:
        mode = st.mode(last_100)
        lower_mode = mode-0.05
        upper_mode = mode+0.05
        upper_freq = last_100.count(upper_mode)
        lower_freq = last_100.count(lower_mode)
        for order in kite.orders()['data']:
                if buy_id == '' and sell_id == '':
                    break
                if order['order_id']==buy_id and order['status']=='COMPLETE':
                    bought = True
                elif order['order_id']==sell_id and order['status']=='COMPLETE':
                    sold = True
        if bought and sold:
            if upper_freq>=lower_freq:
                buy_id = kite_limit_buy('IDEA',mode,3,0)
                sell_id = kite_limit_sell('IDEA',upper_mode,3,0)
                bought = sold = False
            else:
                buy_id = kite_limit_buy('IDEA',lower_mode,3,0)
                sell_id = kite_limit_sell('IDEA',mode,3,0)
                bought = sold = False
        







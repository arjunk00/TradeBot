from stockfunctions import stock_code_to_token, token_to_stock_code
from kite_settings import *
from kiteconnect_trade import *
import statistics as st
import math as mt

N = 20
last_N = []


def on_ticks(ws, ticks):
    for tick in ticks:
        if len(last_N) <= N:
            last_N.append(tick['last_price'])
        else:
            del last_N[0]
            last_N.append(tick['last_price'])


def on_connect(ws, response):
    token = stock_code_to_token('IDEA')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_LTP, [token])


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
    if len(last_N) < N - 1:
        continue
    else:
        mode = st.mode(last_N)
        lower_mode = float(mt.trunc((mode - 0.05) * 100) / 100)
        upper_mode = float(mt.trunc((mode + 0.05) * 100) / 100)
        upper_freq = last_N.count(upper_mode)
        lower_freq = last_N.count(lower_mode)
        for order in kite.orders():
            if buy_id == '' and sell_id == '':
                break
            if order['order_id'] == buy_id and order['status'] == 'COMPLETE':
                bought = True
            elif order['order_id'] == sell_id and order['status'] == 'COMPLETE':
                sold = True
        if bought and sold:
            if upper_freq >= lower_freq:
                buy_id = kite_limit_buy('IDEA', mode, 6, 0)
                sell_id = kite_limit_sell('IDEA', upper_mode, 6, 0)
                bought = sold = False
            else:
                buy_id = kite_limit_buy('IDEA', lower_mode, 6, 0)
                sell_id = kite_limit_sell('IDEA', mode, 6, 0)
                bought = sold = False

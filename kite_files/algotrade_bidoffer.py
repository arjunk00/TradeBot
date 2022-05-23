from tools.stockfunctions import stock_code_to_token
from kite_settings import *
from kiteconnect_trade import *
import statistics as st
import math as mt

N = 50
last_N = []
bidask_info = {'total_bids': 0, 'total_offers': 0}
depth = [1]


def on_ticks(ws, ticks):
    for tick in ticks:
        depth.append(tick['depth'])
        del depth[0]
        if len(last_N) <= N:
            last_N.append(tick['last_price'])
        else:
            del last_N[0]
            last_N.append(tick['last_price'])


def on_connect(ws, response):
    token = stock_code_to_token('IDEA')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_FULL, [token])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect(threaded=True)

buy_id = sell_id = ''
bought = True
sold = True

while True:
    if len(last_N) < N - 1:
        continue
    else:
        mode = st.mode(last_N)
        lower_mode = float(mt.trunc((mode - 0.05) * 100) / 100)
        upper_mode = float(mt.trunc((mode + 0.05) * 100) / 100)
        upper_freq = last_N.count(upper_mode)
        lower_freq = last_N.count(lower_mode)
        if lower_freq < upper_freq:
            currpair = [mode, upper_mode]
        elif lower_freq > upper_freq:
            currpair = [lower_mode, mode]
        else:
            continue
        depth_cur = depth[-1]
        for i in depth_cur['buy']:
            bidask_info['total_bids'] += i['quantity'] * i['orders']
        for j in depth_cur['sell']:
            bidask_info['total_offers'] += i['quantity'] * i['orders']

        for order in kite.orders():
            if buy_id == '' and sell_id == '':
                break
            if order['order_id'] == buy_id and order['status'] == 'COMPLETE':
                bought = True
            elif order['order_id'] == sell_id and order['status'] == 'COMPLETE':
                sold = True
        if bought and sold:
            if bidask_info['total_bids'] < bidask_info['total_offers']:
                buy_id = kite_limit_buy('IDEA', currpair[0] - 0.05, 6,0)
                sell_id = kite_limit_sell('IDEA', currpair[0], 6,0)
                bought = sold = False
            elif bidask_info['total_bids'] > bidask_info['total_offers']:
                buy_id = kite_limit_buy('IDEA', currpair[1], 6,0)
                sell_id = kite_limit_sell('IDEA', currpair[1] + 0.05, 6,0)
                bought = sold = False
            else:
                continue

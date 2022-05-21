from kite_settings import *
from kiteconnect_trade import *
import statistics as st
import math as mt

N = 50
last_N = []


def on_ticks(ws, ticks):
    for tick in ticks:
        # print(type(tick['last_price']))
        if len(last_N) <= N:
            last_N.append(tick['last_price'])
        else:
            del last_N[0]
            last_N.append(tick['last_price'])


def on_connect(ws, response):
    token = 3677697  # stock_code_to_token('IDEA')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_LTP, [token])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect(threaded=True)

while True:
    if len(last_N) < N - 1:
        continue
    else:
        mode = st.mode(last_N)
        lower_mode = float(mt.trunc((mode - 0.05) * 100) / 100)
        upper_mode = float(mt.trunc((mode + 0.05) * 100) / 100)
        upper_freq = last_N.count(upper_mode)
        lower_freq = last_N.count(lower_mode)
        print(lower_mode, lower_freq, upper_mode, upper_freq)
        # if lower_freq>upper_freq:
        #     print(lower_mode)
        # else:
        #     print(upper_mode)

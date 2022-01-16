import logging
from kiteconnect import KiteTicker, KiteConnect
# from kiteconnect_trade import *
import statistics as st
import math as mt

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
request_token = "8H5geKY7Z77BZqziPihTt0PIzMcQiW2h"
# access_token = "dofi017V4RNn7VBe1RPH22oeKf3elDdI"

kite = KiteConnect(api_key=api_key)
print(kite.login_url())
#
data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(data["access_token"])
print(data['access_token'])

kws = KiteTicker(api_key, data["access_token"])

N = 50
last_N = []
bidask_info = {'total_bids':0,'total_asks':0}
depth = [1]

def kite_limit_buy(symbol, price, quantity, stoploss):
    buy_order_id = kite.place_order(exchange=kite.EXCHANGE_NSE,
                                    tradingsymbol=symbol,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_LIMIT,
                                    price=price,
                                    stoploss=stoploss,
                                    validity=kite.VALIDITY_DAY,
                                    variety=kite.VARIETY_REGULAR)
    logging.info("Order placed, order ID is - {}".format(buy_order_id))
    return buy_order_id



def kite_limit_sell(symbol, price, quantity, stoploss):
    sell_order_id = kite.place_order(exchange=kite.EXCHANGE_NSE,
                                     tradingsymbol=symbol,
                                     transaction_type=kite.TRANSACTION_TYPE_SELL,
                                     quantity=quantity,
                                     product=kite.PRODUCT_MIS,
                                     order_type=kite.ORDER_TYPE_LIMIT,
                                     price=price,
                                     stoploss=stoploss,
                                     validity=kite.VALIDITY_DAY,
                                     variety=kite.VARIETY_REGULAR)
    logging.info("Order placed, order ID is - {}".format(sell_order_id))
    return sell_order_id

def cancel_order(orderid):
    kite.cancel_order(
        variety = kite.VARIETY_REGULAR,
        order_id = orderid
    )

def on_ticks(ws, ticks):
    for tick in ticks:
        depth.append(tick['depth'])
        del depth[0]
        if len(last_N)<=N:
            last_N.append(tick['last_price'])
        else:
            del last_N[0]
            last_N.append(tick['last_price'])




def on_connect(ws, response):
    token = 3677697 #stock_code_to_token('IDEA')
    ws.subscribe([token])

    ws.set_mode(ws.MODE_FULL,[token])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect(threaded=True)

while True:
    if len(last_N)<N-1:
        continue
    else:
        mode = st.mode(last_N)
        lower_mode = float(mt.trunc((mode-0.05)*100)/100)
        upper_mode = float(mt.trunc((mode+0.05)*100)/100)
        upper_freq = last_N.count(upper_mode)
        lower_freq = last_N.count(lower_mode)
        if lower_freq<upper_freq:
            currpair = [mode,upper_mode]
        elif lower_freq>upper_freq:
            currpair = [lower_mode,mode]
        else:
            continue
        depth_cur = depth[-1]
        for i in depth_cur['buy']:
            bidask_info['total_bids'] += i['quantity']*i['orders']
        for j in depth_cur['sell']:
            bidask_info['total_asks'] += i['quantity']*i['orders']
        



        

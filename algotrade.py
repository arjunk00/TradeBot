import logging
from kiteconnect import KiteTicker, KiteConnect
# from kiteconnect_trade import *
import statistics as st

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
request_token = "a97veDsjnsKb7ieuGTMeVoq2JF1D1aCj"
# access_token = "dofi017V4RNn7VBe1RPH22oeKf3elDdI"

kite = KiteConnect(api_key=api_key)
print(kite.login_url())
#
data = kite.generate_session(request_token, api_secret=api_secret)
kite.set_access_token(data["access_token"])
print(data['access_token'])

kws = KiteTicker(api_key, data["access_token"])


last_100 = []


def kite_limit_buy(symbol, price, quantity, stoploss):
    buy_order_id = kite.place_order(exchange=kite.EXCHANGE_NSE,
                                    tradingsymbol=symbol,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    product=kite.PRODUCT_MIS,
                                    order_type=kite.ORDER_TYPE_MARKET,
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
                                     order_type=kite.ORDER_TYPE_MARKET,
                                     price=price,
                                     stoploss=stoploss,
                                     validity=kite.VALIDITY_DAY,
                                     variety=kite.VARIETY_REGULAR)
    logging.info("Order placed, order ID is - {}".format(sell_order_id))
    return sell_order_id

def on_ticks(ws, ticks):
    for tick in ticks:
        print(tick)
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
# bought = False
# sold = False
# buy_id = ''
# sell_id = ''
no = 0
while True:
    if len(last_100)<99:
        continue
    else:
        mode = st.mode(last_100)
        lower_mode = mode-0.05
        upper_mode = mode+0.05
        upper_freq = last_100.count(upper_mode)
        lower_freq = last_100.count(lower_mode)
        # for order in kite.orders():
        #         if buy_id == '' and sell_id == '':
        #             break
        #         if order['order_id']==buy_id and order['status']=='COMPLETE':
        #             bought = True
        #         elif order['order_id']==sell_id and order['status']=='COMPLETE':
        #             sold = True

        if upper_freq >= lower_freq:
            if last_100[-1] >= upper_mode:
                if no>=0:
                    sell_id = kite_limit_sell('IDEA', upper_mode, 1, 0)
                    no+=-1
                    # sold = True
            if last_100[-1] <= mode:
                if no<=0:
                    buy_id = kite_limit_buy('IDEA', mode, 1, 0)
                    no+=1
                    # bought = True
        else:
            if last_100[-1] <= lower_mode:
                if no<=0:
                    buy_id = kite_limit_buy('IDEA', lower_mode, 1, 0)
                    no+=1
                    # bought = True
            if last_100[-1] >= mode:
                if no>=0:
                    sell_id = kite_limit_sell('IDEA', mode, 1, 0)
                    no+=-1
                    # sold = True
        







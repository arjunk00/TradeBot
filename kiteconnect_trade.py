import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
request_token = "HmmYxXG4F05fpmNVYfRW6YcrRwQehLQ1"
access_token = "UqgUJ1LCgcDN7kPnAaS3Q2ZfkWjcN1dd"

kite = KiteConnect(api_key=api_key)
print(kite.login_url())

data = kite.generate_session(request_token, api_secret=api_secret)
print(data[access_token])
kite.set_access_token(data[access_token])


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
                                    variety=None)
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


# fetch all orders
kite.orders()

# get list of positions
kite.positions()

kite.holdings()

# fetch instruments
exchange = ['NSE', 'BFO', 'BSE', 'CDS', 'MCX', 'NFO']
kite.instruments(exchange="NSE")

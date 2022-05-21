from kite_settings import *


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
        variety=kite.VARIETY_REGULAR,
        order_id=orderid
    )


# fetch all orders
kite.orders()

# get list of positions
kite.positions()

print(kite.holdings())

# fetch instruments
exchange = ['NSE', 'BFO', 'BSE', 'CDS', 'MCX', 'NFO']
kite.instruments(exchange="NSE")

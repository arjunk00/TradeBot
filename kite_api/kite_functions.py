from kite_api import kite, kws
import logging
import sys, os
import datetime

PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/"
f = open(f"{PROJECT_ROOT_DIR}/logs/logs{datetime.datetime.now().date()}.txt", "w+")
f.close()
logging.basicConfig(filename=f"{PROJECT_ROOT_DIR}/logs/logs{datetime.datetime.now().date()}.txt", level=logging.INFO,
                    filemode='a')
logging.info(f"{datetime.datetime.now()}\thello")


# retrieve your holdings from zerodha account
def show_holdings():
    return kite.holdings()


# retrieve list of tradable instruments according to exchange
def get_instruments(exchange=None):
    return kite.instruments(exchange)


# delete current session
def delete_session(acc_tkn=None):
    return kite.invalidate_access_token(acc_tkn)


# get list of all orders
def show_orders():
    return kite.orders()


# retrieve current positions from zerodha account
def show_positions():
    return kite.positions()


def kite_limit_buy(tradingsymbol, quantity, order_type, price, validity=None, stoploss=None, squareoff=None):
    limit_buy_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                          exchange=kite.EXCHANGE_NSE,
                                          variety=kite.VARIETY_REGULAR,
                                          validity=kite.VALIDITY_DAY,
                                          order_type=kite.ORDER_TYPE_LIMIT,
                                          quantity=quantity,
                                          price=price,
                                          )
    logging.info(f"Limit Buy Order placed, order ID is - {limit_buy_order_id}")
    return limit_buy_order_id


def kite_limit_sell(tradingsymbol, quantity, price, validity=None, stoploss=None, squareoff=None):
    limit_sell_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                           exchange=kite.EXCHANGE_NSE,
                                           variety=kite.VARIETY_REGULAR,
                                           validity=kite.VALIDITY_DAY,
                                           order_type=kite.ORDER_TYPE_LIMIT,
                                           quantity=quantity,
                                           price=price,
                                           transaction_type=kite.TRANSACTION_TYPE_SELL
                                           )
    logging.info(f"Limit Sell Order placed, order ID is - {limit_sell_order_id}")
    return limit_sell_order_id


def kite_market_buy(tradingsymbol, quantity, price, validity=None, stoploss=None, squareoff=None):
    market_buy_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                           exchange=kite.EXCHANGE_NSE,
                                           variety=kite.VARIETY_REGULAR,
                                           validity=kite.VALIDITY_DAY,
                                           order_type=kite.ORDER_TYPE_MARKET,
                                           quantity=quantity,
                                           price=price,
                                           transaction_type=kite.TRANSACTION_TYPE_BUY
                                           )
    logging.info(f"Market Buy Order placed, order ID is - {market_buy_order_id}")
    return market_buy_order_id


def kite_market_sell(tradingsymbol, quantity, price, validity=None, stoploss=None, squareoff=None):
    market_sell_order_id = kite.place_order(tradingsymbol=tradingsymbol,
                                            exchange=kite.EXCHANGE_NSE,
                                            variety=kite.VARIETY_REGULAR,
                                            validity=kite.VALIDITY_DAY,
                                            order_type=kite.ORDER_TYPE_MARKET,
                                            quantity=quantity,
                                            price=price,
                                            transaction_type=kite.TRANSACTION_TYPE_SELL
                                            )
    logging.info(f"Market Sell Order placed, order ID is - {market_sell_order_id}")
    return market_sell_order_id


def get_margins():
    return kite.margins()


def get_ltp(instruments):
    return kite.ltp(instruments)

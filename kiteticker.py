import logging
from kitedata_postgres import *
from kiteconnect import KiteTicker
import time
from stockfunctions import stock_code_to_token 

logging.basicConfig(level=logging.DEBUG)
api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
access_token = "UqgUJ1LCgcDN7kPnAaS3Q2ZfkWjcN1dd"
kws = KiteTicker(api_key, access_token)

tokens = [408065, 73856, 256265, 265]


def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks))
    insert_tick = insert_ticks(ticks)
    print(ticks)


def on_connect(ws, response,stock_code):
    ws.subscribe(list(stock_code_to_token(stock_code)))

    ws.set_mode(ws.MODE_FULL, [stock_code_to_token(stock_code)[0]])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect('INFY')

# count = 0
# while True:
#     if count < len(tokens):
#         if kws.is_connected():
#             logging.info("Subscribing to: {}".format(tokens[count]))
#             kws.subscribe([tokens[count]])
#             kws.set_mode(kws.MODE_LTP, [tokens[count]])
#             count += 1
#         else:
#             logging.info("Connecting to WebSocket...")
#
#     time.sleep(2)

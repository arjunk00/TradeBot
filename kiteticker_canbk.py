import logging
from kitedata_postgres_canbk import *
from kiteconnect import KiteTicker
import time

logging.basicConfig(level=logging.DEBUG)
api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
access_token = "uMyIYRVXusyVmRLVuVy4RgTd2eqfg8Cy"
kws = KiteTicker(api_key, access_token)

tokens = [408065, 73856, 256265, 265]


def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks))
    insert_tick = insert_ticks(ticks)
    print(ticks)


def on_connect(ws, response):
    ws.subscribe([2763265, 10794])

    ws.set_mode(ws.MODE_FULL, [2763265])


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()

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
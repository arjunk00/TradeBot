import logging
from kitedata_postgres import *
from kiteconnect import KiteTicker
from stockfunctions import stock_code_to_token, token_to_stock_code
import csv
import time

logging.basicConfig(level=logging.DEBUG)
api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
access_token = "uMyIYRVXusyVmRLVuVy4RgTd2eqfg8Cy"
kws = KiteTicker(api_key, access_token)

# tokens = [408065, 73856, 256265, 265]


def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks))
    insert_tick = insert_ticks(ticks)
    print(ticks)


def on_connect(ws, response):
    stock1 = ''
    stock2 = ''
    stock3 = ''
    stock4 = ''
    stock5 = ''
    token_list = [stock_code_to_token(stock_code_to_token(stock1),stock_code_to_token(stock2),stock_code_to_token(stock3),stock_code_to_token(stock4),stock_code_to_token(stock5))]
    # with open('ind_nifty200list.csv') as file:
    #     csvreader = csv.reader(file)
    #     n=0
    #     for row in csvreader:
    #         n+=1
    #         if n>5:
    #             break
    #         nifty200_token_list.append(stock_code_to_token(row[2]))


    ws.subscribe(token_list)

    ws.set_mode(ws.MODE_FULL, token_list)


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

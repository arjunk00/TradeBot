import logging
from kitedata_postgres import *
from kiteconnect import KiteTicker
from stockfunctions import stock_code_to_token, token_to_stock_code


# logging.basicConfig(level=logging.DEBUG)
# api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
access_token = "dofi017V4RNn7VBe1RPH22oeKf3elDdI"
kws = KiteTicker(api_key, access_token)

# tokens = [408065, 73856, 256265, 265]


def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks))
    insert_tick = insert_ticks(ticks)
    print(ticks)


def on_connect(ws, response):
    # nifty200_token_list = []
    # with open('ind_nifty200list.csv') as file:
    #     csvreader = csv.reader(file)
    #     n=0
    #     for row in csvreader:
    #         n+=1
    #         if n>5:
    #             break
    #         nifty200_token_list.append(stock_code_to_token(row[2]))
    tokens=[stock_code_to_token('YESBANK'),stock_code_to_token('PNB'),stock_code_to_token('SAIL'),stock_code_to_token('ONGC'),stock_code_to_token('COALINDIA')]

    ws.subscribe(tokens)

    ws.set_mode(ws.MODE_FULL, tokens)


def on_close(ws, code, reason):
    ws.stop()


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()



from kite_settings import *
from kitedata_postgres import *
from kiteconnect import KiteTicker
from tools.stockfunctions import stock_code_to_token, token_to_stock_code


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
    tokens = [stock_code_to_token('IDEA') ,stock_code_to_token('IRCTC'),stock_code_to_token('ITC'),stock_code_to_token('CANBK'),stock_code_to_token('PNB')]

    ws.subscribe(tokens)

    ws.set_mode(ws.MODE_FULL, tokens)


def on_close(ws, code, reason):
    pass


kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()

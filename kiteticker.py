import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)

kws = KiteTicker("your_api_key", "your_access_token")

def on_ticks(ws, ticks):
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    ws.subscribe([738561])
    ws.set_mode(ws.MODE_FULL, [738561])


def on_ticks(ws, ticks):
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    ws.subscribe([738561, 5633])

    ws.set_mode(ws.MODE_FULL, [738561])

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()


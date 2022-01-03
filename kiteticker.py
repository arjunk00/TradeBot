import logging
from kiteconnect import KiteTicker

logging.basicConfig(level=logging.DEBUG)
api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key ="t44a8jbiydzpqq8b"
access_token = "qUhbnHQph0kIfPzQJ4jQjrAS64737em3"
kws = KiteTicker(api_key, access_token)

def on_ticks(ws, ticks):
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    ws.subscribe([738561])
    ws.set_mode(ws.MODE_FULL, [738561])


def on_ticks(ws, ticks):
    logging.debug("Ticks: {}".format(ticks))

def on_connect(ws, response):
    ws.subscribe([408065, 1594])

    ws.set_mode(ws.MODE_LTP, [408065])

    print("\n")

    print("\n")

    print("\n")

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

kws.connect()


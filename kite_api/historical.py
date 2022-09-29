from kiteconnect import KiteConnect, KiteTicker
from kite_login import api_key, api_secret
import os
kite = KiteConnect(api_key)
kws = KiteTicker(api_key, os.environ["accesstoken"])

kws.connect()
if kws.is_connected():
    kws.subscribe([408065, 884737])
    kws.set_mode(kws.MODE_LTP, [408065, 884737])



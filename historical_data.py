import logging
import datetime
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_key = 't44a8jbiydzpqq8b'
api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'

kite = KiteConnect(api_key, api_secret)

print(kite.login_url())

data = kite.generate_session("E6SwRpcRoQrVCBbFzOGPBTSs0iemvIbr", api_secret)
print(data["access_token"])
kite.set_access_token(data["access_token"])


def get_historical_data(from_, to_):
    from_=datetime.datetime(2021, 1, 1, 1, 1, 1)
    to_=datetime.datetime(2022, 1, 1, 1, 1, 1)
    interval="minute"
    historicalData=kite.historical_data("trading token", from_, to_, interval, False, False)
    print(historicalData)

def ltp(token):
    kite.ltp(token)

print(ltp('INFY'))


# kite.historical_data(self, 738561, from_date=2021-01-01 01:01:01)
import logging
import datetime
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_key = 'xxxxxxxxxxxxx'
api_secret = 'xxxxxxxxxxxxx'

kite = KiteConnect(api_key, api_secret)

print(kite.login_url())

data = kite.generate_session("request_token_here", api_secret)
kite.set_access_token(data["access_token"])


def get_historical_data(from_, to_):
    from_=datetime.datetime(2021, 1, 1, 1, 1, 1)
    to_=datetime.datetime(2022, 1, 1, 1, 1, 1)
    interval="minute"
    historicalData=kite.historical_data("trading token", from_, to_, interval, False, False)
    print(historicalData)

def ltp(token):
    kite.ltp(token)


# kite.historical_data(self, 738561, from_date=2021-01-01 01:01:01)
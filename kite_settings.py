import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
request_token = "QzPjE5CtDl41w7NWpwJnuLeE32bjhmO0"
access_token = "5hQI4oo9QSn704JSDJCmkWj0YJjT8xRH"

kite = KiteConnect(api_key)
print(kite.login_url())

data = kite.generate_session(request_token, api_secret)
print(data["access_token"])
kite.set_access_token(data["access_token"])

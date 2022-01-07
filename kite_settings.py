import logging
from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
request_token = "F96lS1lMl2V9vAb8r3ecBqpoYmVFQGGa"
access_token = "dofi017V4RNn7VBe1RPH22oeKf3elDdI"

kite = KiteConnect(api_key)
print(kite.login_url())

data = kite.generate_session(request_token, api_secret)
print(data["access_token"])
kite.set_access_token(data["access_token"])

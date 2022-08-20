from selenium import webdriver
import logging
from kiteconnect import KiteConnect, KiteTicker

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
# access_token = "mOScvzyOX2mSlt3bMSAXX7T2HA824Yoz"

kite = KiteConnect(api_key=api_key)

# print(kite.login_url())
driver = webdriver.Chrome()
driver.get(kite.login_url())
oldurl = driver.current_url

# login to kite after here

while True:
    newurl = driver.current_url
    if oldurl != newurl:
        break
    pass
print(newurl)
# get request token fron url
request_token = newurl[1:2]
access_token = kite.generate_session(request_token, api_secret)['access_token']  # generate access token
kite.set_access_token(access_token)  # set access token, now kite object is ready to use
kws = KiteTicker(api_key, access_token)  # websocket object is also ready to use

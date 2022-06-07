'''
Steps to use kite_settings.py ->
1. Open kite_settings.py.
2. Uncomment the lines starting with print till sys.exit().
3. Run kite_settings.py.
4. In the prompt, click on URL, login using kite, and paste the request token from URL into the prompt.
5. Prompt will generate the access token. Copy it and paste it into its variable above.
6. Comment the above uncommented lines again and use the file wherever u want.
7. For example check all files starting with algotrade_---.py.
'''

import logging
from kiteconnect import KiteConnect, KiteTicker
import sys

logging.basicConfig(level=logging.DEBUG)

api_secret = 'rkvip6z4jhn1fn5rifnrtbh707ukaf8x'
api_key = "t44a8jbiydzpqq8b"
access_token = "mOScvzyOX2mSlt3bMSAXX7T2HA824Yoz"

kite = KiteConnect(api_key=api_key)

# These lines are to be commented and uncommented---------------- START ----------
# print(kite.generate_session(request_token=input(f"Request Token: {kite.login_url()} = "), api_secret=api_secret)['access_token'])
# sys.exit()
# Till Here ------------------------- END -------------------


kite.set_access_token(access_token=access_token)

kws = KiteTicker(api_key, access_token)

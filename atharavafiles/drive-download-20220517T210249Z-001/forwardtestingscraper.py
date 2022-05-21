from stockfunctions import stock_code_to_token, token_to_stock_code, ohlc
import datetime as dt
from tools import webscraper as ws
from pickleextract import *


duration = dt.timedelta(minutes = 1)
stock_code = 'ADANIPORTS'



volticks = ws.VolumeTicker(stock_code,duration,interval)
priceticks = ws.PriceTicker(stock_code,duration,interval)
volticks.start()
priceticks.start()

threshold_dict = {'DRREDDY': 0.41878420750591105, 'HINDUNILVR': 0.43559159507797407,
                  'ADANIPORTS': 0.6452825406318907,'AXISBANK': 0.4541107217201816}

while True:
    if priceticks.pricelistcopy[0] + priceticks.duration <= dt.datetime.now() < priceticks.pricelistcopy[0] + 2*priceticks.duration:
        # this is input at each time stamp (at the end of time)
        # df = ['Open', 'High','Low','Close','Volume']
        df = ohlc(priceticks.pricelistcopy[1:])
        df.append(volticks.vollistcopy[-1]-volticks.vollistcopy[1])
        linregobj = regobj(stock_code) 
        up_prob = linregobj.predict(df) # denoted as alpha in pdf
        if up_prob > threshold_dict[stock_code]:
            if df[0] > df[3]:
                print("B")
            else:
                print("H")
        else:
            if df[0] > df[3]:
                print("H")
            else:
                print("B")
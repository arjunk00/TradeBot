import sys
sys.path.insert(0,'/home/fernblade/TradeBot/tools')
from stockfunctions import ohlc
import datetime as dt
import webscraper as ws
from pickleextract import *
import numpy as np
import csv


duration = dt.timedelta(minutes = 5)
stock_code = 'DRREDDY'


# writer.writerows([['Date','Time','Open','High','Low','Close','Signal','Price','alpha']])

volticks = ws.VolumeTicker(stock_code,duration,1)
priceticks = ws.PriceTicker(stock_code,duration,1)
volticks.start()
priceticks.start()

threshold_dict = {'DRREDDY': 0.41878420750591105, 'HINDUNILVR': 0.43559159507797407,
                  'ADANIPORTS': 0.6452825406318907,'AXISBANK': 0.4541107217201816}

while True:
    if priceticks.pricelistcopy == []:
        # print("waiting for data")
        continue
    elif priceticks.pricelistcopy[0] + priceticks.duration <= dt.datetime.now() <= priceticks.pricelistcopy[0] + 2*priceticks.duration:
        # this is input at each time stamp (at the end of time)
        # df = ['Open', 'High','Low','Close','Volume']
        df = ohlc(priceticks.pricelistcopy[1:])
        df.append(volticks.vollistcopy[-1]-volticks.vollistcopy[1])
        dfarr = np.array(df,ndmin=2)
        linregobj = regobj(stock_code) 
        up_prob = linregobj.predict(dfarr)[0][0] # denoted as alpha in pdf
        if up_prob > threshold_dict[stock_code]:
            if df[0] > df[3]:
                print("B")
                signal = "B"
            else:
                print("H")
                signal = None
        else:
            if df[0] > df[3]:
                print("H")
                signal = None
            else:
                print("S")
                signal = "S"
        with open('drreddytest.csv','a+') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow([priceticks.pricelistcopy[0].date(),priceticks.pricelistcopy[0].time(),df[0],df[1],df[2],df[3],signal,priceticks.pricelistcopy[-1],up_prob])
        priceticks.pricelistcopy = []
    else:
        print("You shouldnt be here")
from nsetools import Nse
from nsepy import get_history
from datetime import date
import simplerbank as sbi
import csv
import math
import datetime
nse = Nse()

def fallbuy(stock_code):
    data = get_history(symbol=stock_code, start=date(2019,1,1), end=date(2020,1,1))['Close']
    prevavg = data.mean()
    datacov = get_history(symbol=stock_code, start=date(2020,3,1), end=date(2021,3,1))['Close']
    covavg = datacov.mean()
    expectedreturn = (prevavg-covavg)*100/covavg
    fallperc = (prevavg-covavg)*100/prevavg
    q = nse.get_quote(stock_code)['lastPrice']
    if q < prevavg:
        return (stock_code,True,expectedreturn,fallperc,prevavg,covavg,prevavg-covavg)
    else:
        return (stock_code,False,expectedreturn,fallperc,prevavg,covavg,prevavg-covavg)

def yearlyreturn(profit_percent,time):
    t = time.total_seconds()
    k = datetime.timedelta(365).total_seconds()
    return (((1+(profit_percent/100))**(k/t))-1)*100
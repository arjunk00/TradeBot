from nsetools import Nse
from nsepy import get_history
from datetime import date
import simplerbank as sbi
import csv
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
        return (True,expectedreturn,fallperc,prevavg,covavg,prevavg-covavg)
    else:
        return (False,expectedreturn,fallperc,prevavg,covavg,prevavg-covavg)

print(fallbuy('INFY'))
"""
with open('Screener_Results.csv') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel')
    n = 0
    for row in spamreader:
        if n == 0:
            n+=1
            continue
        else:
            print(row)
            print(fallbuy(row[1]))


"""

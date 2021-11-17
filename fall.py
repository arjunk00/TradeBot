from nsetools import Nse
from nsepy import get_history
from datetime import date
import simplerbank as sbi
nse = Nse()
stock_code = "CCHHL"
data = get_history(symbol=stock_code, start=date(2019,1,1), end=date(2020,1,1))['Close']
prevavg = data.mean()
datacov = get_history(symbol=stock_code, start=date(2020,3,1), end=date(2021,3,1))['Close']
covavg = datacov.mean()
print(prevavg,covavg,prevavg-covavg,(prevavg-covavg)*100/prevavg,(prevavg-covavg)*100/covavg)
q = nse.get_quote(stock_code)['lastPrice']
if q < prevavg*0.9:
    print("Buy")
else:
    print("Don't")
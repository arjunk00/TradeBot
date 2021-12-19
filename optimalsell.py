from stockfunctions import *

stock_code = 'INFY'
now = datetime.datetime.now()
t = 300
buy_price = nse.get_quote(stock_code)['lastPrice']
while datetime.datetime.now()-now < datetime.timedelta(0,t):
    p = (nse.get_quote(stock_code)['lastPrice']-buy_price)*100/buy_price
    print(yearlyreturn(p,datetime.now()-now))


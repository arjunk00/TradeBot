from tools.stockfunctions import *
import matplotlib.pyplot as plt
stock_code = 'INFY'
now = datetime.datetime.now()
t = 300
buy_price = nse.get_quote(stock_code)['lastPrice']
Y = []
X = []
while datetime.datetime.now()-now < datetime.timedelta(0,t):
    p = (nse.get_quote(stock_code)['lastPrice']-buy_price)*100/buy_price
    Y.append(yearlyreturn(p,datetime.datetime.now()-now))
    X.append(datetime.datetime.now())
plt.scatter(X,Y)
plt.show()


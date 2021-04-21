from nsetools import Nse
from threading import *
nse = Nse()
def fakelivealert(stock_code,alert_price):
    alert_price = 55
    q1 = 0 #nse.get_quote(code)['lastPrice']
    q2 = 0 #nse.get_quote(code)['lastPrice']
    L = [q1,q2]
    q = 0
    while True:
        q +=2 #nse.get_quote(code)['lastPrice']
        del L[0]
        L.append(q)
        if (L[0]<=alert_price<=L[1] or L[1]<=alert_price<=L[0]):
            print('target price reached for '+stock_code)
            break
        print(stock_code+":",q)
def livealert(stock_code,alert_price):
    q1 = nse.get_quote(stock_code)['lastPrice']
    q2 = nse.get_quote(stock_code)['lastPrice']
    L = [q1,q2]
    while True:
        q = nse.get_quote(stock_code)['lastPrice']
        del L[0]
        L.append(q)
        if (L[0]<=alert_price<=L[1] or L[1]<=alert_price<=L[0]):
            print('target price reached for '+stock_code)
            break
        print(stock_code+":",q)

class Eyeofmehta(Thread):
    def __init__(self, stock_code,alert_price):
        Thread.__init__(self)
        self.stock_code = stock_code
        self.alert_price = alert_price

    def run(self):
        fakelivealert(self.stock_code, self.alert_price)

stockalertdict = {'infy':55,'poty':23,'hemlo':77}
for key, val in stockalertdict.items():
    t = Eyeofmehta(key,val)
    t.start()

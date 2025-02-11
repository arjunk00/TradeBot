import mysql.connector as sqltor
from nsetools import Nse
import math
nse = Nse()
class Demataccount:
    def __init__(self,user,balance):
        self.user = user
        self.balance = balance
        self.assets = self.Assets()

    def market_buy(self,stock_code,**kwargs): # max (bool), buy_qty (int)
        max = kwargs['max']
        curprice = float(nse.get_quote(stock_code)['lastPrice'])
        self.assets.last_buyprice = curprice
        maxbuy = math.floor(self.balance/curprice)
        if max:
            buy_qty = maxbuy
            self.assets.stock_code = stock_code
            self.assets.qty_owned += buy_qty
            self.balance -= buy_qty*curprice
        
        else:
            buy_qty = kwargs['buy_qty']
            if buy_qty>maxbuy:
                print("not enough balance for buy")
            else:
                self.assets.stock_code = stock_code
                self.assets.qty_owned += buy_qty
                self.balance -= buy_qty*curprice
    
    def market_sell(self,stock_code,**kwargs): # max (bool), buy_qty (int)
        max = kwargs['max']
        curprice = float(nse.get_quote(stock_code)['lastPrice'])
        if max:
            sell_qty = self.assets.qty_owned
            self.assets.qty_owned -= sell_qty
            self.balance += sell_qty*curprice
        else:
            sell_qty = kwargs['sell_qty']
            if sell_qty>self.assets.qty_owned:
                print("cant sell more than you have")
            else:
                self.assets.qty_owned -= sell_qty
                self.balance += sell_qty*curprice

    def limit_buy(self,stock_code,**kwargs): #max (bool), bid (float), buy_qty (int)
        max = kwargs['max']
        buy_price = kwargs['bid']
        maxbuy = math.floor(self.balance/buy_price)
        if max:
            buy_qty = maxbuy
        elif kwargs['buy_qty'] <= maxbuy:
            buy_qty = kwargs['buy_qty']
        else:
            print("Insufficient funds")
            return None
        while True:
            curprice = float(nse.get_quote(stock_code)['lastPrice'])
            if curprice <= buy_price:
                self.assets.stock_code = stock_code
                self.assets.qty_owned += buy_qty
                self.balance -= buy_qty*buy_price
                break
    
    def limit_sell(self,stock_code,**kwargs): #max (bool), bid (float), buy_qty (int)
        pass

    def networth(self):
        stock_code = self.assets.stock_code
        qty_owned = self.assets.qty_owned
        curprice = float(nse.get_quote(stock_code)['lastPrice'])
        return curprice*qty_owned
    
    def percentchange(self):
        stock_code = self.assets.stock_code
        lastprice = self.assets.last_buyprice
        curprice = float(nse.get_quote(stock_code)['lastPrice'])
        return (curprice-lastprice)*100/lastprice

        
    class Assets:
        def __init__(self):
            self.stock_code = ''
            self.qty_owned = 0
            self.last_buyprice = 0
        

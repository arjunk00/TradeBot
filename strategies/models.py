from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np
from tools.stockfunctions import marubozu
import datetime as dt

class DoubleLogit:
    def __init__(self,name):
        self.name = name
        self.logitbuy = LogisticRegression(random_state=0)
        self.logitsell = LogisticRegression(random_state=0)
    def train(self,X,y):
        Xbuy = []
        ybuy = []
        Xsell = []
        ysell = []
        for row, output in zip(X,y):
            if row[0]>=row[3]:
                Xbuy.append(row)
                ybuy.append(output)
            else:
                Xsell.append(row)
                ysell.append(output)
        Xbuyarr = np.array(Xbuy)
        ybuyarr = np.array(ybuy)
        Xsellarr = np.array(Xsell)
        ysellarr = np.array(ysell)
        print(Xsellarr.shape)
        print(ysellarr.shape)
        self.logitbuy.fit(Xbuyarr,ybuyarr)
        self.logitsell.fit(Xsellarr,ysellarr)
        print("Training complete")
    def predict(self,X):
        if X[0][0]>=X[0][-2]:
            return self.logitbuy.predict(X)
        else:
            return self.logitsell.predict(X)
    def predict_proba(self,X):
        if X[0][0]>=X[0][-2]:
            return self.logitbuy.predict_proba(X)
        else:
            return self.logitsell.predict_proba(X)

                
class Marubozu:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def predict(self, X):
        # X = ['o','h','l','c']
        output = marubozu(self.stock_code, X)
        if(output['bull']==True):
            return 1
        elif(output['bull']==False):
            return 0
        else:
            return 0.5

class DipDetect:
    def __init__(self, dip_percent: float, price_history: list, current_datetime: dt.datetime):
        '''price_history: list of pairs of datetime and price [(datetime1,price1),....]
        '''
        self.dip_percent = dip_percent
        self.price_history = price_history
        self.current_datetime = current_datetime
        self.last_month_avg = 0
        self.n = 0

    def calc_last_month_avg(self):
        one_month = dt.timedelta(weeks=4)
        start_date = self.current_datetime - one_month
        last_month_avg = 0
        n = 0
        for date_time, price in self.price_history:
            if date_time >= start_date:
                n += 1
                last_month_avg += price
        last_month_avg /= n
        self.last_month_avg = last_month_avg
        self.n = n
    
    def update_last_month_avg(self,newest_removed_price, current_price):
        '''Only to be called if monthly avg has been calculated correctly once'''
        self.last_month_avg += (current_price-newest_removed_price)/self.n

    def update_new_price(self, price, new_datetime):
        self.price_history.append((new_datetime,price))
        self.current_datetime = new_datetime
        one_month = dt.timedelta(weeks=4)
        if self.price_history[0][0] = self.current_datetime - one_month:
            self.calc_last_month_avg()
        elif self.price_history[0][0] > self.current_datetime - one_month:
            l = len(self.price_history)
            newest_removed_price = self.price_history[l-n-1]
            del self.price_history[:l-n]
            self.update_last_month_avg(newest_removed_price,current_price)
        else:
            pass



    def predict(self,current_price):
        change =  (current_price - self.last_month_avg)/self.last_month_avg
        if change <= self.dip_percent:
            return "B"
        elif change >= -self.dip_percent:
            return "S"
        else:
            return "H"




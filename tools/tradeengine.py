from datetime import datetime as dt, timedelta
import csv
import pandas as pd
from tools.brokerage_calc import brokerage_deductions

class TradeEngine:
    def __init__(self,stock_code,initial_capital,outfile):
        self.stock_code = stock_code
        self.qty = 0
        self.funds = initial_capital #update every order and end of each day add t-2 margin
        self.margin = {} #update every order and delete first after t+2
        self.blockedmargin = 0
        self.leverage = 5
        self.current_datetime = dt.now() #update at every row
        self.csvwriter = csv.writer(outfile)
        self.daytradesdataframe = pd.DataFrame({'symbol':[],'datetime':[],'order':[],'quantity':[],'price':[]})
    
    def buy(self,price,qty):
        leveraged_price = price/self.leverage
        max_qty = self.funds//leveraged_price
        if qty == 'max':
            qty = max_qty
        if qty > max_qty:
            raise Exception("Not enough funds to buy")
        if leveraged_price*qty > self.funds or leveraged_price*qty <= 0:
            raise Exception("Out of funds")
        self.blockedmargin += leveraged_price*qty
        self.funds -= self.blockedmargin
        self.qty += qty

        #['symbol','datetime','order','qty','price','funds','totalcapital']
        row = [
            self.stock_code,
            self.current_datetime,
            'B',
            qty,
            price,
            self.funds,
            None
        ]
        self.csvwriter.writerow(row)
        df = self.daytradesdataframe
        df.loc[len(df.index)] = row[:5]

    def short(self,price,qty):
        leveraged_price = price/self.leverage
        max_qty = self.funds//leveraged_price
        if qty == 'max':
            qty = max_qty
        if qty > max_qty:
            raise Exception("Not enough funds to buy")
        if leveraged_price*qty > self.funds or leveraged_price*qty <= 0:
            raise Exception("Out of funds")
        self.blockedmargin = leveraged_price*qty
        self.funds -= self.blockedmargin
        self.qty -= qty

        #['symbol','datetime','order','qty','price','funds','totalcapital']
        row = [
            self.stock_code,
            self.current_datetime,
            'S',
            qty,
            price,
            self.funds,
            None
        ]
        self.csvwriter.writerow(row)
        df = self.daytradesdataframe
        df.loc[len(df.index)] = row[:5]

    def sell(self,price,qty):
        max_qty = self.qty
        if qty == 'max':
            qty = max_qty
        elif qty > max_qty:
            raise Exception("Cannot short using sell function")

        PL =  price*qty - self.leverage*self.blockedmargin*(qty/max_qty)
        self.funds += self.blockedmargin*(qty/max_qty)
        self.blockedmargin -= self.blockedmargin*(qty/max_qty)
        self.qty -= qty
        if PL > 0:
            self.margin[self.current_datetime.date()] += PL
        else:
            self.funds += PL
        
        #['symbol','datetime','order','qty','price','funds','totalcapital']
        if self.qty == 0:
            totalcapital = self.funds
        else:
            totalcapital = None
        row = [
            self.stock_code,
            self.current_datetime,
            'S',
            qty,
            price,
            self.funds,
            totalcapital
        ]
        self.csvwriter.writerow(row)
        df = self.daytradesdataframe
        df.loc[len(df.index)] = row[:5]

    def squareoff(self,price,qty):
        max_qty = -self.qty
        if qty == 'max':
            qty = max_qty
        elif qty > max_qty:
            raise Exception("Can't buy with this function")
        
        PL = self.leverage*self.blockedmargin*(qty/max_qty) - price*qty
        self.funds += self.blockedmargin
        self.blockedmargin -= self.blockedmargin*(qty/max_qty)
        self.qty += qty
        if PL > 0:
            self.margin[self.current_datetime.date()] += PL
        else:
            self.funds += PL
        
        #['symbol','datetime','order','qty','price','funds','totalcapital']
        if self.qty == 0:
            totalcapital = self.funds
        else:
            totalcapital = None
        row = [
            self.stock_code,
            self.current_datetime,
            'B',
            qty,
            price,
            self.funds,
            totalcapital
        ]
        self.csvwriter.writerow(row)
        df = self.daytradesdataframe
        df.loc[len(df.index)] = row[:5]
    
    def posexit(self,price):
        if self.qty > 0:
            self.sell(price,'max')
        elif self.qty < 0:
            self.squareoff(price,'max')
    
    def daychange(self):
        # print(brokerage_deductions(self.daytradesdataframe)['deduction'])
        self.funds += list(self.margin.values())[0]# - brokerage_deductions(self.daytradesdataframe)['deduction']
        del self.margin[list(self.margin.keys())[0]]
        self.margin[self.current_datetime.date()] = 0
        self.daytradesdataframe = pd.DataFrame({'symbol':[],'datetime':[],'order':[],'quantity':[],'price':[]})
    
    def setdatetime(self,date,time):
        date_time = date+time
        self.current_datetime = dt.strptime(date_time,'%Y-%m-%d%H:%M:%S')
        if len(self.margin.keys()) == 0:
            self.margin[self.current_datetime.date()-timedelta(days=1)] = 0
            self.margin[self.current_datetime.date()-timedelta(days=2)] = 0


    
# outfile = open('trailorderbook.csv','w',newline='')
# obj = TradeEngine('ADANIPORTS',10,outfile)
# obj.short(10,'max')
# obj.short(10,'max')
# obj.short(10,'max')
        
        
        


        



        

        
        

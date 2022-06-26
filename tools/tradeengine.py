from datetime import datetime as dt, timedelta
import csv

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
    
    def buy(self,price,qty):
        leveraged_price = price/self.leverage
        max_qty = self.funds//leveraged_price
        if qty == 'max':
            qty = max_qty
        elif qty > max_qty:
            raise Exception("Not enough funds to buy")
        
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

    def short(self,price,qty):
        leveraged_price = price/self.leverage
        max_qty = self.funds//leveraged_price
        if qty == 'max':
            qty = max_qty
        elif qty > max_qty:
            raise Exception("Not enough funds to buy")

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
            'S',
            qty,
            price,
            self.funds,
            totalcapital
        ]
        self.csvwriter.writerow(row)
    
    def daychange(self):
        self.funds += self.margin[self.current_datetime.date()-timedelta(days=2)] #-deductable()
        del self.margin[self.current_datetime.date()-timedelta(days=2)]
        self.margin[self.current_datetime.date()] = 0
    
    def setdatetime(self,date,time):
        date_time = date+time
        self.current_datetime = dt.strptime(date_time,'%Y-%m-%d%H:%M:%S')
        if len(self.margin.keys()) == 0:
            self.margin[self.current_datetime.date()-timedelta(days=1)] = 0
            self.margin[self.current_datetime.date()-timedelta(days=2)] = 0


    
    
        
        
        
        
        


        



        

        
        

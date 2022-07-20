import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../../"
sys.path.append(PROJECT_ROOT_DIR)
print(PROJECT_ROOT_DIR)

from tools.tradeengine import TradeEngine
import csv
import datetime as dt

class OrderBook:
    def __init__(self,stock_code):
        self.stock_code = stock_code
        self.infile = open(f'{os.path.dirname(os.path.realpath(__file__))}/../adanisignal.csv','r')
        self.outfile = open(f'{os.path.dirname(os.path.realpath(__file__))}/adaniorderbook.csv','w',newline='')
        self.csvreader = csv.reader(self.infile)
        self.engine = TradeEngine(stock_code,10000,self.outfile)


    def run(self):
        engine = self.engine
        for row in self.csvreader:
            lastdate = engine.current_datetime.date()
            engine.setdatetime(row[0],row[1])
            curdate = engine.current_datetime.date()
            if engine.current_datetime.time() >= dt.time(15,15):
                engine.posexit(float(row[-2]))
                continue
            if lastdate != curdate:
                engine.daychange()
            if row[-3] == 'B':
                if engine.qty == 0:
                    engine.buy(float(row[-2]),'max')
                elif engine.qty < 0:
                    engine.squareoff(float(row[-2]),'max')
                    engine.buy(float(row[-2]),'max')
            elif row[-3] == 'S':
                if engine.qty == 0:
                    engine.short(float(row[-2]),'max')
                elif engine.qty > 0:
                    engine.sell(float(row[-2]),'max')
                    engine.short(float(row[-2]),'max')
             

class DollarCostAvg:
    def __init__(self,stock_code):
        self.stock_code = stock_code
        self.infile = open(f'{os.path.dirname(os.path.realpath(__file__))}/trailsignal.csv','r')
        self.outfile = open(f'{os.path.dirname(os.path.realpath(__file__))}/trailorderbook.csv','w',newline='')
        self.csvreader = csv.reader(self.infile)
        self.engine = TradeEngine(stock_code,10000,self.outfile)
    
    def run(self):
        engine = self.engine
        for row in self.csvreader:




# order = OrderBook('ADANIPORTS')
# order.run()


        


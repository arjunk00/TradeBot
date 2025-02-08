from tools.tradeengine import *

outfile = open("trades.csv","a")
engine = TradeEngine("TCS",10000,outfile)
engine.setdatetime("2025-02-10","10:00:00")
engine.leverage = 1
engine.buy(69,10)
engine.sell(70,10)
engine.daychange()
engine.buy(71,1)
engine.sell(70,1)
engine.daychange()
engine.daychange()
engine.daychange()
engine.buy(1,1)
engine.sell(1,1)



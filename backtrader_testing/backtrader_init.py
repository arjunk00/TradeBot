import backtrader as bt

class Strategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def log(self,txt,dt=None):
        dt=dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}{txt}')

    def next(self):
        self.log(' %.2f' % self.dataclose[0])

cerebro = bt.Cerebro()

data = bt.feeds.YahooFinanceCSVData(dataname = "RELIANCE.NS.csv")
cerebro.adddata(data)

cerebro.addstrategy(Strategy)
cerebro.run()
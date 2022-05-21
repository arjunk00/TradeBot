import backtrader as bt
class MAcrossover(bt.Strategy):
    # Moving average parameters
    params = (('pfast', 20), ('pslow', 50),)

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()} {txt}')  # Comment this line when running optimization

    def __init__(self):
        self.dataclose = self.datas[0].close

        # Order variable will contain ongoing order details/status
        self.order = None

        # Instantiate moving averages
        self.slow_sma = bt.indicators.MovingAverageSimple(self.datas[0],
                                                          period=self.params.pslow)
        self.fast_sma = bt.indicators.MovingAverageSimple(self.datas[0],
                                                          period=self.params.pfast)
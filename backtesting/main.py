import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.append(PROJECT_ROOT_DIR)

from signal_generator import SignalGenLinReg, SignalGenMarubozu
from backtesting.orderbook.orderbookgenerator import OrderBook
from tradebook.tradebook_generator import tradebook_generator
test = SignalGenLinReg('BAJFINANCE')
test.run()

test = OrderBook('BAJFINANCE')
test.run()
#
# tradebook_generator(f"{test.stock_code}orderbook")
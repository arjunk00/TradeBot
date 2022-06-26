import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.append(PROJECT_ROOT_DIR)

from signal_generator import BackTest
from backtesting.orderbook.orderbookgenerator import OrderBook
# test = BackTest('ADANIPORTS')
# test.run()

test = OrderBook('ADANIPORTS')
test.run()

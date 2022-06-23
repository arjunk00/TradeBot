import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.append(PROJECT_ROOT_DIR)

import sqlite3
from tools.dbhelper import createordertable

class OrderBook:
    def __init__(self,stock_code):
        self.stock_code = stock_code

    def run(self):
        conn = sqlite3.connect(f"{PROJECT_ROOT_DIR}/backtesting/backtestdatabase.db")
        cursor = conn.cursor()
        createordertable(self.stock_code,cursor)
        

        


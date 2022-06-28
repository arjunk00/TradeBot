import warnings
warnings.filterwarnings("ignore")

import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.append(PROJECT_ROOT_DIR)

from tools.stockfunctions import createsignaltable, store
import pickle
import datetime as dt
import numpy as np
import csv
import sqlite3
from pickleextract_backtest import log_reg_obj



class BackTest:
    def __init__(self, stock_code):
        super().__init__()
        # self.duration = duration
        self.stock_code = stock_code

    def run(self):
        # conn = sqlite3.connect(f"{PROJECT_ROOT_DIR}/backtesting/trial.db")
        # cursor = conn.cursor()
        # createsignaltable(self.stock_code, cursor)
        # conn.commit()
        signalcsvfile = open(f"{os.path.dirname(os.path.realpath(__file__))}/trailsignal.csv","w",newline='')
        csvwriter = csv.writer(signalcsvfile)
#0.6423560850684784
        threshold_dict = {
            "DRREDDY": 0.41713667119195574,
            "HINDUNILVR": 0.4300811185876499,
            "ADANIPORTS": 0.5,
            "AXISBANK": 0.4525515696307913,
            "APOLLOHOSP": 0.6086177020679596,
            "BHARTIARTL": 0.4082868996895255,
            "ICICIBANK": 0.2612070711103042,
            "TATASTEEL": 0.5850011395166405,
            "BAJFINANCE": 0.598080106955147,
            "TATAMOTORS": 0.6552967288547805,
            "INFY": 0.5342662493071376,
            "ASIANPAINT": 0.3757896383910965
        }

        # prices_and_volume = getPricesandVolume(self.stock_code, self.duration)

        testfile =  open(f'{os.path.dirname(os.path.realpath(__file__))}/ADANIPORTS__EQ__NSE__NSE__5MINUTE_CONVERGED.csv', 'r')
        datareader = csv.reader(testfile)
        for row in datareader:
            prices_and_volume = row[1:]
            # print(prices_and_volume)
            prices_and_volume = [float(x) for x in prices_and_volume]

            print(prices_and_volume)

            if prices_and_volume is None:
                pass

            prices_and_volume_arr = np.array(prices_and_volume, ndmin=2)
            # prices_and_volume_arr = prices_and_volume_arr.astype(np.float64)
            logregobj = log_reg_obj(self.stock_code)
            up_prob = logregobj.predict_proba(prices_and_volume_arr)[0][1]

            if up_prob > threshold_dict[self.stock_code]:
                if prices_and_volume[0] > prices_and_volume[3]:
                    print("B")
                    signal = "B"
                    date_time = row[0]
                else:
                    print("H")
                    signal = None
                    date_time = row[0]
            else:
                if prices_and_volume[0] > prices_and_volume[3]:
                    print("H")
                    signal = None
                    date_time = row[0]
                else:
                    print("S")
                    signal = "S"
                    date_time = row[0]

            row = [
                str(date_time)[0:10],
                str(date_time)[11:19],
                prices_and_volume[0],
                prices_and_volume[1],
                prices_and_volume[2],
                prices_and_volume[3],
                signal,
                prices_and_volume[3],
                up_prob
            ]

            csvwriter.writerow(row)
            # store(self.stock_code, tuplelist, cursor)
            print(self.stock_code, row)
            # conn.commit()
        signalcsvfile.close()
        testfile.close()


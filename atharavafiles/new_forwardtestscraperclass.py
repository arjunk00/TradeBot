import warnings
warnings.filterwarnings("ignore")

import sys, os
PROJECT_ROOT_DIR = f"{os.path.dirname(os.path.realpath(__file__))}/../"
sys.path.append(PROJECT_ROOT_DIR)

import sqlite3
import datetime as dt
import numpy as np
from threading import Thread
from atharavafiles.pickleextract import regobj
from tools.stockfunctions import createsignaltable, store
from tools.new_webscraper import getPricesandVolume

class ForwardTest(Thread):
	def __init__(self, stock_code, duration):
		super().__init__()
		self.duration = duration
		self.stock_code = stock_code
	
	def run(self):
		conn = sqlite3.connect(f"{PROJECT_ROOT_DIR}/databases/test1.db")
		cursor = conn.cursor()

		createsignaltable(self.stock_code, cursor)
		conn.commit()

		threshold_dict = {
			"DRREDDY": 0.41878420750591105, 
			"HINDUNILVR": 0.43559159507797407,
			"ADANIPORTS": 0.6452825406318907, 
			"AXISBANK": 0.4541107217201816,
			"APOLLOHOSP": 0.6086177020679596, 
			"BHARTIARTL": 0.4082868996895255,
			"ICICIBANK": 0.2612070711103042, 
			"TATASTEEL": 0.5850011395166405,
		}

		prices_and_volume = getPricesandVolume(self.stock_code, self.duration)
		
		if prices_and_volume is None:
			pass

		prices_and_volume_arr = np.array(prices_and_volume, ndmin=2)
		linregobj = regobj(self.stock_code)
		up_prob = linregobj.predict(prices_and_volume_arr)[0][0]

		if up_prob > threshold_dict[self.stock_code]:
			if prices_and_volume[0] > prices_and_volume[3]:
				print("B")
				signal = "B"
				date_time = dt.datetime.now()
			else:
				print("H")
				signal = None
				date_time = dt.datetime.now()
		else:
			if prices_and_volume[0] > prices_and_volume[3]:
				print("H")
				signal = None
				date_time = dt.datetime.now()
			else:
				print("S")
				signal = "S"
				date_time = dt.datetime.now()

		tuplelist = (
			str(date_time.date()),
			str(date_time.time()),
			prices_and_volume[0],
			prices_and_volume[1],
			prices_and_volume[2],
			prices_and_volume[3],
			signal,
			prices_and_volume[3],
			up_prob,
		)

		store(self.stock_code, tuplelist, cursor)
		print(self.stock_code, tuplelist)
		conn.commit()

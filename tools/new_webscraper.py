from numpy import Infinity
import requests 
import json
import datetime as dt

def getPricesandVolume(stock_code, duration = 5, max_retries = 10):
	"""
	Returns prices and volume in a duration as ["open", "high", "low", "close", "volume"]
	
	Duration is the time period in minutes for which OHLCV values are calculated
	"""

	current_timestamp = int(dt.datetime.now().timestamp())
	#current_timestamp = 1655285000
	#print(current_timestamp, dt.datetime.fromtimestamp(current_timestamp))
	last_duration_timestamp = current_timestamp - (current_timestamp % (60*duration))
	period1 = last_duration_timestamp - 60*duration - 60
	period2 = last_duration_timestamp + 60
	#print(period1, dt.datetime.fromtimestamp(period1))
	#print(period2, dt.datetime.fromtimestamp(period2))

	url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stock_code}.NS?period1={period1}&period2={period2}&region=US&lang=en-US&includePrePost=false&interval=1m&useYfid=true&corsDomain=finance.yahoo.com&.tsrc=finance"
	#print(url)
	header = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
		"Accept-Encoding":	"gzip, deflate, br",
		"Accept-Language":	"en-US,en;q=0.5",
		"Connection":	"keep-alive",
		"Host":	"query1.finance.yahoo.com",
		"Sec-Fetch-Dest":	"document",
		"Sec-Fetch-Mode":	"navigate",
		"Sec-Fetch-Site":	"none",
		"Sec-Fetch-User":	"?1",
		"TE":	"trailers",
		"Upgrade-Insecure-Requests":	"1",
		"User-Agent":	"code",
	}

	while max_retries != 0:
		#print(int(dt.datetime.timestamp(dt.datetime.now())))
		r = requests.get(url, headers=header)
		r = json.loads(r.text)
		#print(r)
		
		start_timestamp = period1 + 60
		end_timestamp = period2 - 60
		try:
			returned_timestamps = r["chart"]["result"][0]["timestamp"]
		except KeyError:
			#print("No return value")
			max_retries -= 1
			continue

		if start_timestamp not in returned_timestamps or end_timestamp not in returned_timestamps:
			continue
		break
	
	if max_retries == 0:
		return None

	start_index = r["chart"]["result"][0]["timestamp"].index(start_timestamp)
	end_index = r["chart"]["result"][0]["timestamp"].index(end_timestamp) - 1
	return_value = r["chart"]["result"][0]["indicators"]["quote"][0]

	volume = sum(list(map(lambda x: 0 if (x == None) else x, return_value["volume"][start_index:end_index+1])))
	prices = [
		return_value["open"][start_index],
		max(list(map(lambda x: -Infinity if(x == None) else x, return_value["high"][start_index:end_index+1]))),
		min(list(map(lambda x: Infinity if(x == None) else x, return_value["low"][start_index:end_index+1]))),
		return_value["close"][end_index],
	]
	
	#print(volume)
	#print(prices)
	return prices + [volume]

getPricesandVolume("DRREDDY", 5)

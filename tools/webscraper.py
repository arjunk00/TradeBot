import requests
from bs4 import BeautifulSoup
import time
from threading import *
import datetime as dt

class VolumeTicker(Thread):
    def __init__(self, symbol,duration,interval):
        super().__init__()
        self.stock_code = symbol
        self.vollist = []
        self.interval = interval
        self.duration = duration
        self.vollistcopy = self.vollist
    def run(self):
        while True:
            url = "https://finance.yahoo.com/quote/"+self.stock_code+".NS?p="+self.stock_code+".NS&.tsrc=fin-srch"
            # https: // finance.yahoo.com / quote / DRREDDY.NS?p = DRREDDY.NS &.tsrc = fin - srch
            r=requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            fetch = soup.find('td', {'data-test': 'TD_VOLUME-value'}).text

            s1 = fetch.translate({ord(','): None})
            volume = int(s1)
            if len(self.vollist) == 0:
                self.vollist.append(dt.datetime.now())
                self.vollist.append(volume)
            elif dt.datetime.now() <= self.vollist[0] + self.duration:
                self.vollist.append(volume)
            elif dt.datetime.now() > self.vollist[0] + self.duration:
                self.vollistcopy = self.vollist
                self.vollist = []
            
            time.sleep(self.interval)
        

class PriceTicker(Thread):
    def __init__(self, symbol,duration,interval):
        super().__init__()
        self.stock_code = symbol
        self.pricelist = []
        self.duration = duration
        self.interval = interval
        self.pricelistcopy = []
    def run(self):
        while True:
            url = "https://www.google.com/finance/quote/"+self.stock_code+":NSE"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            fetch = soup.find('div', {'class': 'YMlKec fxKbKc'}).text

            price_string = (fetch[1:])
            s1 = price_string.translate({ord(','): None})

            price = float(s1)
            if len(self.pricelist) == 0:
                self.pricelist.append(dt.datetime.now())
                self.pricelist.append(price)
            elif dt.datetime.now() <= self.pricelist[0] + self.duration:
                self.pricelist.append(price)
            elif dt.datetime.now() > self.pricelist[0] + self.duration:
                self.pricelistcopy = self.pricelist
                self.pricelist = []
            time.sleep(self.interval)
# relpricescrap = PriceTicker('RELIANCE',dt.timedelta(seconds=30), 1)
# volscrap = VolumeTicker('RELIANCE',dt.timedelta(seconds = 30), 1)
# relpricescrap.start()
# volscrap.start()
# while True:
#     # print(relpricescrap.pricelist)
#     print(volscrap.vollist)
#     time.sleep(1)

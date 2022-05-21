import requests
from bs4 import BeautifulSoup
import time
from threading import *
prices =[]
volumes = []
class VolumeTicker(Thread):
    def __init__(self, symbol):
        super().__init__()
        self.stock_code = symbol
    def run(self):
        while True:
            url = "https://finance.yahoo.com/quote/"+self.stock_code+".NS?p="+self.stock_code+".NS&.tsrc=fin-srch"
            r=requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            fetch = soup.find('td', {'data-test':'TD_VOLUME-value'}).text

            s1 = fetch.translate({ord(','): None})
            volume = int(s1)
            volumes.append(volume)
            time.sleep(1)

class PriceTicker(Thread):
    def __init__(self, symbol):
        super().__init__()
        self.stock_code = symbol
    def run(self):
        while True:
            url = "https://www.google.com/finance/quote/"+self.stock_code+":NSE"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')

            fetch = soup.find('div', {'class': 'YMlKec fxKbKc'}).text

            price_string = (fetch[1:])
            s1 = price_string.translate({ord(','): None})

            price = float(s1)
            prices.append(price)
            time.sleep(1)
relscrap = PriceTicker('RELIANCE')
relscrap.start()
while True:
    print(prices)
    time.sleep(1)

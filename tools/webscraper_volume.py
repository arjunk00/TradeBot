import requests
from bs4 import BeautifulSoup
import time
from threading import *

volumes = []
class print_volume(Thread):
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


relscrap = print_volume('RELIANCE')
relscrap.start()
while True:
    print(volumes)
    time.sleep(1)

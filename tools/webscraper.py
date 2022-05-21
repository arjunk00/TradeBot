import requests
from bs4 import BeautifulSoup
import time
from csv import writer
import csv

prices = []
while True:
    url = "https://www.google.com/finance/quote/BTC-USD"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    fetch = soup.find('div', {'class': 'YMlKec fxKbKc'}).text
    volume = soup.find('p', {'class': 'h5Ghwc-IOpRCf'}).text

    price_string = (fetch[0:])
    s1 = price_string.translate({ord(','): None})

    price = float(s1)
    prices.append(price)
    print(price)
    print(volume)
    with open('test.csv', 'a+') as file:
        reader = csv.reader(file)
        next(reader, None)
        writer_obj = writer(file, delimiter=',')
        writer_obj.writerow(prices)
    prices.clear()
    time.sleep(2)

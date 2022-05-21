from nsetools import Nse
import datetime
import simplerbank as sbi
import statistics as st
nse = Nse()
stock_code = 'zomato'
principle_investment = 100000
guptedemat = sbi.Demataccount('Gupte',principle_investment)

L=[]
n=50
while True:
    q = nse.get_quote(stock_code)['lastPrice']
    L.append(q)
    size = len(L)
    if size > n:
        L.pop(0)
    elif size < n:
        continue
    else:
        M = st.mean(L)
        
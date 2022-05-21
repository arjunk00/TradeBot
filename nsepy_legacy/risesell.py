from nsetools import Nse
import datetime
import simplerbank as sbi
nse = Nse()
stock_code = 'zomato'
principle_investment = 10000
guptedemat = sbi.Demataccount('Gupte',principle_investment)
guptedemat.buy(stock_code,max=True)
while True:
    paisa = guptedemat.networth()+guptedemat.balance
    print(paisa)
    if paisa <= principle_investment*0.99:
        guptedemat.sell(stock_code,max=True)
        break 
    if guptedemat.percentchange()>0.8:
        guptedemat.sell(stock_code, max=True)
    elif guptedemat.percentchange()<0.4:
        guptedemat.buy(stock_code,max=True)
    else:
        now = datetime.datetime.now()
        market_close = datetime.datetime(2021,9,21,15,30)
        if now<market_close:
            continue
        else:
            break

print("Final networth: ",guptedemat.networth())
print("Final Balance: ",guptedemat.balance)
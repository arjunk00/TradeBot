from nsetools import Nse
import datetime
import simplerbank as sbi
nse = Nse()
stock_code = 'zomato'
principle_investment = 100000
guptedemat = sbi.Demataccount('Gupte',principle_investment)

q1 = nse.get_quote(stock_code)['lastPrice']
q2 = nse.get_quote(stock_code)['lastPrice']
L = [q1,q2]
rise = [True,True]
guptedemat.buy(stock_code,max=True)
while True:
    print(guptedemat.networth()+guptedemat.balance)
    now = datetime.datetime.now()
    market_close = datetime.datetime(2021,9,22,15,30)
    if now>market_close:
        print("Final networth: ",guptedemat.networth())
        print("Final Balance: ",guptedemat.balance)
        break
        
    del L[0], rise[0]
    q = nse.get_quote(stock_code)['lastPrice']
    L.append(q)
    if L[0]<L[1]:
        rise.append(True)
    elif L[0]>L[1]:
        rise.append(False)
    else:
        rise.append(rise[0])
    
    if rise[0] and rise[1]:
        guptedemat.buy(stock_code,max=True)
    elif (not rise[0] ) and (not rise[1]):
        guptedemat.sell(stock_code, max=True)


'''print(guptedemat.networth()+guptedemat.balance)
now = datetime.datetime.now()
        market_close = datetime.datetime(2021,9,21,15,30)
        if now>market_close:
            continue
        else:
            print("Final networth: ",guptedemat.networth())
            print("Final Balance: ",guptedemat.balance)
            break'''
    
    


    
    


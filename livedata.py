from nsetools import Nse
nse = Nse()
code = 'infy'
alert_price = 55
q1 = 0 #nse.get_quote(code)['lastPrice']
q2 = 0 #nse.get_quote(code)['lastPrice']
L = [q1,q2]
q = 0
while True:
    q +=2 #nse.get_quote(code)['lastPrice']
    del L[0]
    L.append(q)
    if (L[0]<=alert_price<=L[1] or L[1]<=alert_price<=L[0]):
        print('target price reached')
        break
    print(q)


from stockfunctions import *
M = 0
with open('Equity.csv') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel')
    first = True
    day = datetime.date(2021,10,1)
    while day<=datetime.date(2021,10,30):
        for row in spamreader:
            if first:
                first = False
                continue
            else:
                stock_code = row[0]
                maru = marubozu(stock_code,day)
                if maru['marubozu']:
                    M += 1
                    print(maru)
        day+=datetime.timedelta(1)
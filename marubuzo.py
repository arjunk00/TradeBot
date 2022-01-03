from stockfunctions import marubozu
import csv
import datetime
M = 0
print(marubozu("PARAS", datetime.date(2021, 10, 12)))


with open('Equity.csv') as csvfile:
    spamreader = csv.reader(csvfile, dialect='excel')
    first = True
    day = datetime.date(2021,10,1)
<<<<<<< HEAD
    while day<=datetime.date(2021,10,29):
=======
    while day<=datetime.date(2021,10,30):
>>>>>>> b852c00746b3a0ed663a99d7e5a7592f88eb2d5a
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



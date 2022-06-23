import models as md
import csv
import numpy as np
import datetime as dt
import pickle
def makepickle(obj,picklename):
    filename = picklename
    outfile = open("strategies/trainedpickles/"+filename,'wb')
    pickle.dump(obj,outfile)
    outfile.close()

stock_code = "ADANIPORTS"
trainingdatafile = open("strategies\\trainingdata\\processed\\{}__EQ__NSE__NSE__5MINUTE_TRAINING.csv".format(stock_code),"r")
csvreader = csv.reader(trainingdatafile)
next(csvreader)
Xlst = []
ylst = []
n = 0
for row in csvreader:
    n += 1
    print(row)
    Xrow = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])]
    ydata = row[-1]
    Xlst.append(Xrow)
    ylst.append(int(ydata))
    datetimestr = row[0][:19]
    datetimeobj = dt.datetime.strptime(datetimestr, '%Y-%m-%d %H:%M:%S')
    #2018-05-03
    if datetimeobj >= dt.datetime(year=2018,month=5,day=2):
        break
X = np.array(Xlst)
y = np.array(ylst)
adanidoublelogit = md.DoubleLogit(stock_code)
adanidoublelogit.train(X,y)
makepickle(adanidoublelogit,'DOUBLELOGIT_5MIN_TRAINED_{}'.format(stock_code))
trainingdatafile.close()

print(adanidoublelogit.predict(np.array([[268.15,269.4,267.75,269.4,30605.0]])))

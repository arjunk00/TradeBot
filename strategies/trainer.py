import models as md
import csv
import numpy as np

stock_code = "ADANIPORTS"
trainingdatafile = open(r"strategies\\trainingdata\\processed\\ADANIPORTS__EQ__NSE__NSE__MINUTE_TRAINING.csv","r")
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
    ylst.append(ydata)
X = np.array(Xlst)
y = np.array(ylst)
adanidoublelogit = md.DoubleLogit(stock_code)
adanidoublelogit.train(X,y)
trainingdatafile.close()


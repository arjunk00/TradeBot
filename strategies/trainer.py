import os
import models as md
import csv
import numpy as np
import datetime as dt
import pickle
def makepickle(obj,picklename):
    filename = picklename
    outfile = open(f"{os.path.dirname(os.path.realpath(__file__))}/trainedpickles/{filename}.pickle",'wb')
    pickle.dump(obj,outfile)
    outfile.close()

if __name__=="__main__":
    stock_code = "ADANIPORTS"
    trainingdatafile = open(f"{os.path.dirname(os.path.realpath(__file__))}/trainingdata/processed/{stock_code}__EQ__NSE__NSE__5MINUTE_TRAINING_LINREG.csv","r")
    csvreader = csv.reader(trainingdatafile)
    next(csvreader)
    Xlst = []
    ylst = []
    n = 0
    for row in csvreader:
        n += 1
        print(row)
        # Xrow = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])]
        Xrow = [float(row[1]),float(row[2]),float(row[3]),float(row[4])]
        ydata = row[-1]
        Xlst.append(Xrow)
        ylst.append(float(ydata))
        datetimestr = row[0][:19]
        datetimeobj = dt.datetime.strptime(datetimestr, '%Y-%m-%d %H:%M:%S')
        #2018-05-03
        if datetimeobj >= dt.datetime(year=2018,month=5,day=2):
            break
    X = np.array(Xlst)
    y = np.array(ylst)
    adanilinregnew = md.LinearReg(stock_code)
    adanilinregnew.train(X,y)
    makepickle(adanilinregnew,f'LINREGNEW_5MIN_TRAINED_{stock_code}')
    trainingdatafile.close()

    # print(adanilinregnew.predict_proba(np.array([[268.15,269.4,267.75,269.4,30605.0]])))

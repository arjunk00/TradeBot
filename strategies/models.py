from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import metrics
import numpy as np
import pandas as pd
from tools.stockfunctions import marubozu
import random


class DoubleLogit:
    def __init__(self, name):
        self.name = name
        self.logitbuy = LogisticRegression(random_state=0)
        self.logitsell = LogisticRegression(random_state=0)

    def train(self, X, y):
        Xbuy = []
        ybuy = []
        Xsell = []
        ysell = []
        for row, output in zip(X, y):
            if row[0] >= row[3]:
                Xbuy.append(row)
                ybuy.append(output)
            else:
                Xsell.append(row)
                ysell.append(output)
        Xbuyarr = np.array(Xbuy)
        ybuyarr = np.array(ybuy)
        Xsellarr = np.array(Xsell)
        ysellarr = np.array(ysell)
        print(Xsellarr.shape)
        print(ysellarr.shape)
        self.logitbuy.fit(Xbuyarr, ybuyarr)
        self.logitsell.fit(Xsellarr, ysellarr)
        print("Training complete")

    def predict(self, X):
        if X[0][0] >= X[0][-2]:
            return self.logitbuy.predict(X)
        else:
            return self.logitsell.predict(X)

    def predict_proba(self, X):
        if X[0][0] >= X[0][-2]:
            return self.logitbuy.predict_proba(X)
        else:
            return self.logitsell.predict_proba(X)


class Marubozu:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def predict(self, X):
        # X = ['o','h','l','c']
        output = marubozu(self.stock_code, X)
        if (output['bull'] == True):
            return 1
        elif (output['bull'] == False):
            return 0
        else:
            return 0.5


class RandomSignals:
    def __init__(self):
        pass

    def predict(self):
        signal = random.randrange(3)
        if signal == 2:
            return 1
        elif signal == 1:
            return 0.5
        else:
            return 0


class LinearReg:
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.lr = LinearRegression()

    def train(self, X, y):
        self.lr.fit(X, y)
        print("training complete")

    def predict(self, X):
        return self.lr.predict(X)

from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np

class DoubleLogit:
    def __init__(self,name):
        self.name = name
        self.logitbuy = LogisticRegression(random_state=0)
        self.logitsell = LogisticRegression(random_state=0)
    def train(self,X,y):
        Xbuy = []
        ybuy = []
        Xsell = []
        ysell = []
        for row, output in zip(X,y):
            if row[0]>=row[3]:
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
        self.logitbuy.fit(Xbuyarr,ybuyarr)
        self.logitsell.fit(Xsellarr,ysellarr)
        print("Training complete")
    def predict(self,X):
        if X[0]>=X[-2]:
            return self.logitbuy.predict(X)
        else:
            return self.logitsell.predict(X)
            

                




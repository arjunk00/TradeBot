from sklearn.linear_model import LogisticRegression, LinearRegression
import numpy as np
import sympy as sy


# from tools.stockfunctions import marubozu
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
        if X[0][0]>=X[0][-2]:
            return self.logitbuy.predict(X)
        else:
            return self.logitsell.predict(X)
    def predict_proba(self,X):
        if X[0][0]>=X[0][-2]:
            return self.logitbuy.predict_proba(X)
        else:
            return self.logitsell.predict_proba(X)

                
class Marubozu:
    def __init__(self, stock_code):
        self.stock_code = stock_code

    def predict(self, X):
        # X = ['o','h','l','c']
        output = marubozu(self.stock_code, X)
        if(output['bull']==True):
            return 1
        elif(output['bull']==False):
            return 0
        else:
            return 0.5

class Baysian:
    def __init__(self,stock_code,f,pi,thetarange):
        self.stock_code = stock_code
        self.f = f #f(x_samp,theta)
        self.pi = pi #pi(theta)
        self.thetarange = thetarange
    
    def m(self,x_samp):
        theta = sy.Symbol("theta")
        return sy.integrate(self.f(x_samp,theta)*self.pi(theta),(theta,self.thetarange[0],self.thetarange[1]))

    def pi_x(self,theta,x_samp):
        return self.f(x_samp,theta)*self.pi(theta)/self.m(x_samp)
    
    def Etheta_pi_x(self,x_samp):
        thetadiscrete = np.linspace(self.thetarange[0],self.thetarange[1],int((self.thetarange[1]-self.thetarange[0])/0.1))
        E = 0
        for theta in thetadiscrete:
            E += theta*self.pi_x(theta,x_samp)
        return E



def f(x,theta):
    return (x/theta)**2

def pi(theta):
    return -theta
        
bay = Baysian('ad',f,pi,[0.5,1])

print(bay.Etheta_pi_x(1))
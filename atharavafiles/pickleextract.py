import pickle
import os

def regobj(stock_code):
    linregobj = pickle.load(open(f'{os.path.dirname(os.path.realpath(__file__))}/linear_regression {stock_code} .pickle','rb'))
    return linregobj
import pickle
def regobj(stock_code):
    linregobj = pickle.load(open('atharavafiles\\linear_regression '+stock_code+'.pickle','rb'))
    return linregobj
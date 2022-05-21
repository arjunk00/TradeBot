import pickle
def regobj(stock_code):
    linregobj = pickle.load(open('atharavafiles\\drive-download-20220517T210249Z-001\\linear_regression '+stock_code+'.pickle','rb'))
    return linregobj
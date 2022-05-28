import pickle
def regobj(stock_code):
    linregobj = pickle.load(open('/home/fernblade/TradeBot/atharavafiles/linear_regression_'+stock_code+'.pickle','rb'))
    return linregobj
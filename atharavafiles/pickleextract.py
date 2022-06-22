import pickle
import os

def regobj(stock_code):
  linregobj = pickle.load(open(f'{os.path.dirname(os.path.realpath(__file__))}/linear_regression_{stock_code}.pickle','rb'))
  return linregobj

def makepickle(obj,picklename):
    filename = picklename
    outfile = open("strategies/trainedpickles/"+filename,'wb')
    pickle.dump(obj,outfile)
    outfile.close()


import pickle
import os
import sys
sys.path.append(rf'{os.path.dirname(os.path.realpath(__file__))}/../strategies/')

def log_reg_obj(stock_code):
  log_reg_obj = pickle.load(open(f'{os.path.dirname(os.path.realpath(__file__))}/pickles/DOUBLELOGIT_5MIN_TRAINED_{stock_code}.pickle','rb'))
  return log_reg_obj

def makepickle(obj,picklename):
    filename = picklename
    outfile = open("strategies/trainedpickles/"+filename,'wb')
    pickle.dump(obj,outfile)
    outfile.close()


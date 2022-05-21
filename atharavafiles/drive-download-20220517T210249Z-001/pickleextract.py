import pickle
linregobj = pickle.load(open('atharavafiles\\drive-download-20220517T210249Z-001\\linear_regression AXISBANK.pickle','rb'))
print(linregobj.score())
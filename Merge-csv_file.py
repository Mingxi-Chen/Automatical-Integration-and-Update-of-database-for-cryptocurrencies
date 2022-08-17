# This python file is to merge all data for cryptocurrencies into a file and label their names
# Author: Mingxi Chen Mx.Chen.official@outlook.com
import glob
import os
import pandas as pd

mycsvdir = 'PATH OF CSV FILES'
csvfiles = glob.glob(os.path.join(mycsvdir,'*.csv'))
dataframes = []

# @parameter name: the file name
for csvfile in csvfiles:
    name = csvfile[33:][:-8]
    print(name)
    df = pd.read_csv(csvfile,index_col=False)
    df.insert(0,column = 'Asset',value=name)
    dataframes.append(df)

result = pd.concat(dataframes)
result.to_csv('top200_test.csv',index=False)

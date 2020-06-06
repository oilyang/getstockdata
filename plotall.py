import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('instance.csv',encoding='gbk')#gbk for Chinese

#list all the code of data
def getCodeList():
    codelist = df['code'].drop_duplicates()
    #for code in codelist:
    #    print(code)
    return codelist
	
def plotAllInOnePic(codelist):
    sn = 0
    a = 0
    for code in codelist:
        single = df[(df['code']==code)][['code','cprice','date']]
        if sn == 0:
            a = single.plot(x='date',y='cprice',label=code)
        else:
            b = single.plot(x='date',y='cprice',label=code,ax=a)
            a = b
        sn = sn + 1
    plt.show()

if __name__ == '__main__':
    codelist = getCodeList()
    plotAllInOnePic(codelist)

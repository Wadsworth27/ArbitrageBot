
import yfinance as yf
import pandas as pd
import math
msft= yf.Ticker('MSFT')
'def createDataFrame(ticker,optionDate)'
print(msft.option_chain('2021-01-29'))
datalist= str(msft.option_chain('2021-01-29')).split()
columns=datalist[0:3] +['Last Sell Time']+datalist[3:15]
cleanRows=[]
baseline=15
for i in range(0,math.floor(len(datalist)/16)-1):
    cleanRows.append(list(datalist[baseline:baseline+16]))
    baseline+=16
df=pd.DataFrame(data=cleanRows,columns=columns)
df.to_csv('msftoptions.csv')


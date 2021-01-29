import yfinance as yf
import pandas as pd
import math
def BuildDataFrame(ticker,expdate):
    #date format '2021-01-29' ticker format 'MSFT'
    symbol= yf.Ticker(ticker)
    datalist= str(symbol.option_chain(expdate)).split()
    columns=datalist[0:3] +['Last Sell Time']+datalist[3:15]
    cleanRows=[]
    baseline=15
    for i in range(0,math.floor(len(datalist)/16)-1):
        cleanRows.append(list(datalist[baseline:baseline+16]))
        baseline+=16
    return pd.DataFrame(data=cleanRows,columns=columns)

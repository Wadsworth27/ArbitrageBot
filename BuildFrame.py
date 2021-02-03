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
    calls_and_puts= pd.DataFrame(data=cleanRows,columns=columns)
    calls_and_puts.rename({'Options(calls=': 'Id'}, axis=1, inplace=True)
    puts=int(calls_and_puts[calls_and_puts['Id']=='puts='].index.values)
    put_frame=calls_and_puts.iloc[puts+1:]
    put_frame.columns=['UniqueID','last trade date','last trade time','strike','lastPrice','bid','ask','change','percentChange','volume','openInterest','impliedVolatility','inTheMoney','contractSize','currency','drop']
    put_frame.reset_index(inplace=True)
    call_frame=calls_and_puts.iloc[:puts]
    put_frame.drop('drop',axis=1)
    call_frame.insert(0,'Exp Date',expdate)
    put_frame.insert(0,'Exp Date',expdate)
    call_frame.insert(0,'Ticker',ticker)
    put_frame.insert(0,'Ticker',ticker)
    call_frame.insert(0,'Option Type','Call')
    put_frame.insert(0,'Option Type','Put')
    return call_frame, put_frame
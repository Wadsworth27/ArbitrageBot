
import yfinance as yf
import pandas as pd
import math
from BuildFrame import BuildDataFrame
import time

#Test 1


def CallArbitrageHunter(lst):
    strikelist= lst[0]['strike'].tolist()
    arbitrageOpps=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):           
            for strike in strikelist:
                try:
                    bid=float(lst[i][lst[i]['strike']==strike]['bid'])
                    ask=float(lst[j][lst[j]['strike']==strike]['ask'])
                    if bid>ask:
                        option1exp =str(lst[i].loc[1,'Exp Date'])
                        option2exp =str(lst[j].loc[1,'Exp Date'])
                        oppSize= str(round((bid-ask)*100))
                        formatedString="The {} and {} ${} Strike represents a ${} arbitrage opportunity".format(option1exp,option2exp,strike,oppSize)
                        arbitrageOpps.append(formatedString)
                except:
                        continue
    for opp in arbitrageOpps:
        print(opp)
start_time = time.time()
MSFT20210205call ,MSFT20210205put = BuildDataFrame('MSFT','2021-02-05')
MSFT20210212call ,MSFT20210212put = BuildDataFrame('MSFT','2021-02-12')
MSFT20210219call ,MSFT20210219put = BuildDataFrame('MSFT','2021-02-19')
MSFT20210226call ,MSFT20210226put = BuildDataFrame('MSFT','2021-02-26')
MSFT20210305call ,MSFT20210305put = BuildDataFrame('MSFT','2021-03-05')
MSFT20210319call ,MSFT20210319put = BuildDataFrame('MSFT','2021-03-19')
MSFT20210416call ,MSFT20210416put = BuildDataFrame('MSFT','2021-04-16')


CallArbitrageHunter([MSFT20210205call, MSFT20210212call, MSFT20210219call, MSFT20210226call, MSFT20210305call, MSFT20210319call, MSFT20210416call] )
print("--- %s seconds ---" % (time.time() - start_time))
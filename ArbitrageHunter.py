from tkinter import messagebox
from datetime import datetime

def ArbitrageHunter(lst):
    strikelist= lst[0]['strike'].tolist()
    arbitrageOpps=[]
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):           
            for strike in strikelist:
                try:
                    bid=float(lst[i][lst[i]['strike']==strike]['bid'])
                    ask=float(lst[j][lst[j]['strike']==strike]['ask'])
                    if bid>ask:
                        ticker=str(lst[i].loc[1,'Ticker'])
                        option1exp =str(lst[i].loc[1,'Exp Date'])
                        option2exp =str(lst[j].loc[1,'Exp Date'])
                        oppSize= str(round((bid-ask)*100))
                        formatedString="{}:The {} and {} ${} Strike represents a ${} arbitrage opportunity".format(ticker,option1exp,option2exp,strike,oppSize)
                        arbitrageOpps.append(formatedString)
                except:
                        continue
    for opp in arbitrageOpps:
        print(opp)
    if arbitrageOpps:
        time=datetime.now().time().strftime('%H:%M:%S')
        messagebox.showinfo('ARBITRAGE OPPORTUNITY', 'PLEASE CHECK THE CONSOLE! An Arbitrage Opportunity has been found on {} at {}'.format(ticker,time))
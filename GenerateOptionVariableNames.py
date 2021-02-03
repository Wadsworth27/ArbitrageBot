#Enter invalid date into BuildFrame and yahoo will return list of avalible option dates
#Enter that list plus the stock ticker for a list of variable names to store the corresponding call and put data frames

def GenerateOptionfunctions(ticker,dates):
    calls=[]
    puts =[]
    for date in dates:
        print(ticker+str(date).replace('-','').strip()+'call ,'+ticker+str(date).replace('-','').strip()+'put = BuildDataFrame('+"'"+ticker+"'"+',\''+date.strip()+'\')')
        calls.append(ticker+str(date).replace('-','').strip()+'call')
        puts.append(ticker+str(date).replace('-','').strip()+'put')  
    callsForHunter= str(calls).replace("'","")
    putsForHunter=str(puts).replace("'","")
    print('ArbitrageHunter('+callsForHunter+')')
    print('ArbitrageHunter('+putsForHunter+')')
GenerateOptionfunctions('DD','2021-02-05, 2021-02-12, 2021-02-19, 2021-02-26, 2021-03-05, 2021-03-12, 2021-03-19, 2021-04-16, 2021-07-16, 2022-01-21, 2023-01-20'.split(','))

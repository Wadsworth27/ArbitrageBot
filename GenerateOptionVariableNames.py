#Enter invalid date into BuildFrame and yahoo will return list of avalible option dates
#Enter that list plus the stock ticker for a list of variable names to store the corresponding call and put data frames

def GenerateOptionfunctions(ticker,dates):
    calls=[]
    for date in dates:
        print(ticker+str(date).replace('-','').strip()+'call ,'+ticker+str(date).replace('-','').strip()+'put = BuildDataFrame('+"'"+ticker+"'"+',\''+date.strip()+'\')')
        calls.append(ticker+str(date).replace('-','').strip()+'call') 
    print(str(calls).replace("'",""))
GenerateOptionfunctions('MSFT','2021-02-05, 2021-02-12, 2021-02-19, 2021-02-26, 2021-03-05, 2021-03-19, 2021-04-16, 2021-06-18, 2021-07-16, 2021-09-17, 2022-01-21, 2022-03-18, 2022-06-17, 2022-09-16, 2023-01-20, 2023-03-17'.split(','))
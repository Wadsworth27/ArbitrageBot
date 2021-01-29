
import yfinance as yf
import pandas as pd
import math
from BuildFrame import BuildDataFrame

df= BuildDataFrame('O','2021-02-19')
df.rename({'Options(calls=': 'Id'}, axis=1, inplace=True)
print(int(df[df['Id']=='puts='].index.values))

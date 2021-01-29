
import yfinance as yf
import pandas as pd
import math
from BuildFrame import BuildDataFrame

#Test 1

MSFTCalls,MSFTputs= BuildDataFrame('MSFT','2021-02-19')
print(MSFTCalls[MSFTCalls['strike']=='205.0']['bid'])
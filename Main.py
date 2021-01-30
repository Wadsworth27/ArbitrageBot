from BuildFrame import BuildDataFrame
from ArbitrageHunter import ArbitrageHunter
import time

#Test 1


start_time = time.time()

PRTY20210219call ,PRTY20210219put = BuildDataFrame('MRO','2021-02-19')
PRTY20210319call ,PRTY20210319put = BuildDataFrame('PRTY','2021-03-19')
PRTY20210416call ,PRTY20210416put = BuildDataFrame('PRTY','2021-04-16')
PRTY20210716call ,PRTY20210716put = BuildDataFrame('PRTY','2021-07-16')
PRTY20220121call ,PRTY20220121put = BuildDataFrame('PRTY','2022-01-21')
PRTY20230120call ,PRTY20230120put = BuildDataFrame('PRTY','2023-01-20')
ArbitrageHunter([PRTY20210219call, PRTY20210319call, PRTY20210416call, PRTY20210716call, PRTY20220121call, PRTY20230120call])
ArbitrageHunter([PRTY20210219put, PRTY20210319put, PRTY20210416put, PRTY20210716put, PRTY20220121put, PRTY20230120put])
time.sleep(10)
print("Operation took %s seconds ---" % (time.time() - start_time))
MRO20210205call ,MRO20210205put = BuildDataFrame('MRO','2021-02-05')
MRO20210212call ,MRO20210212put = BuildDataFrame('MRO','2021-02-12')
MRO20210219call ,MRO20210219put = BuildDataFrame('MRO','2021-02-19')
MRO20210226call ,MRO20210226put = BuildDataFrame('MRO','2021-02-26')
MRO20210305call ,MRO20210305put = BuildDataFrame('MRO','2021-03-05')
MRO20210319call ,MRO20210319put = BuildDataFrame('MRO','2021-03-19')
MRO20210416call ,MRO20210416put = BuildDataFrame('MRO','2021-04-16')
MRO20210618call ,MRO20210618put = BuildDataFrame('MRO','2021-06-18')
MRO20210716call ,MRO20210716put = BuildDataFrame('MRO','2021-07-16')
MRO20210917call ,MRO20210917put = BuildDataFrame('MRO','2021-09-17')
MRO20220121call ,MRO20220121put = BuildDataFrame('MRO','2022-01-21')
MRO20230120call ,MRO20230120put = BuildDataFrame('MRO','2023-01-20')
ArbitrageHunter([MRO20210205call, MRO20210212call, MRO20210219call, MRO20210226call, MRO20210305call, MRO20210319call, MRO20210416call, MRO20210618call, MRO20210716call, MRO20210917call, MRO20220121call, MRO20230120call])
ArbitrageHunter([MRO20210205put, MRO20210212put, MRO20210219put, MRO20210226put, MRO20210305put, MRO20210319put, MRO20210416put, MRO20210618put, MRO20210716put, MRO20210917put, MRO20220121put, MRO20230120put])
print("Operation took %s seconds ---" % (time.time() - start_time))
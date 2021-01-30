from BuildFrame import BuildDataFrame
from ArbitrageHunter import ArbitrageHunter
import time

#Test 1


start_time = time.time()

GE20210212call ,GE20210212put = BuildDataFrame('GE','2021-02-05')
GE20210219call ,GE20210219put = BuildDataFrame('GE','2021-02-19')
ArbitrageHunter([GE20210212call,GE20210219call])
time.sleep(1)
print("Operation took %s seconds ---" % (time.time() - start_time))
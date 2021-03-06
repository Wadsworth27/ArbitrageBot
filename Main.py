from BuildFrame import BuildDataFrame
from ArbitrageHunter import ArbitrageHunter
import time
import yfinance

#Test 1
while True:
    
    start_time = time.time()
    DD20210205call ,DD20210205put = BuildDataFrame('DD','2021-02-05')
    DD20210212call ,DD20210212put = BuildDataFrame('DD','2021-02-12')
    DD20210219call ,DD20210219put = BuildDataFrame('DD','2021-02-19')
    DD20210226call ,DD20210226put = BuildDataFrame('DD','2021-02-26')
    DD20210305call ,DD20210305put = BuildDataFrame('DD','2021-03-05')
    DD20210312call ,DD20210312put = BuildDataFrame('DD','2021-03-12')
    DD20210319call ,DD20210319put = BuildDataFrame('DD','2021-03-19')
    DD20210416call ,DD20210416put = BuildDataFrame('DD','2021-04-16')
    DD20210716call ,DD20210716put = BuildDataFrame('DD','2021-07-16')
    DD20220121call ,DD20220121put = BuildDataFrame('DD','2022-01-21')
    DD20230120call ,DD20230120put = BuildDataFrame('DD','2023-01-20')
    ArbitrageHunter([DD20210205call, DD20210212call, DD20210219call, DD20210226call, DD20210305call, DD20210312call, DD20210319call, DD20210416call, DD20210716call, DD20220121call, DD20230120call])
    ArbitrageHunter([DD20210205put, DD20210212put, DD20210219put, DD20210226put, DD20210305put, DD20210312put, DD20210319put, DD20210416put, DD20210716put, DD20220121put, DD20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))

    AMC20210205call ,AMC20210205put = BuildDataFrame('AMC','2021-02-05')
    AMC20210212call ,AMC20210212put = BuildDataFrame('AMC','2021-02-12')
    AMC20210219call ,AMC20210219put = BuildDataFrame('AMC','2021-02-19')
    AMC20210226call ,AMC20210226put = BuildDataFrame('AMC','2021-02-26')
    AMC20210305call ,AMC20210305put = BuildDataFrame('AMC','2021-03-05')
    AMC20210312call ,AMC20210312put = BuildDataFrame('AMC','2021-03-12')
    AMC20210319call ,AMC20210319put = BuildDataFrame('AMC','2021-03-19')
    AMC20210618call ,AMC20210618put = BuildDataFrame('AMC','2021-06-18')
    AMC20210917call ,AMC20210917put = BuildDataFrame('AMC','2021-09-17')
    AMC20220121call ,AMC20220121put = BuildDataFrame('AMC','2022-01-21')
    AMC20230120call ,AMC20230120put = BuildDataFrame('AMC','2023-01-20')
    ArbitrageHunter([AMC20210205call, AMC20210212call, AMC20210219call, AMC20210226call, AMC20210305call, AMC20210312call, AMC20210319call, AMC20210618call, AMC20210917call, AMC20220121call, AMC20230120call])
    ArbitrageHunter([AMC20210205put, AMC20210212put, AMC20210219put, AMC20210226put, AMC20210305put, AMC20210312put, AMC20210319put, AMC20210618put, AMC20210917put, AMC20220121put, AMC20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))

    NOK20210205call ,NOK20210205put = BuildDataFrame('NOK','2021-02-05')
    NOK20210212call ,NOK20210212put = BuildDataFrame('NOK','2021-02-12')
    NOK20210219call ,NOK20210219put = BuildDataFrame('NOK','2021-02-19')
    NOK20210226call ,NOK20210226put = BuildDataFrame('NOK','2021-02-26')
    NOK20210305call ,NOK20210305put = BuildDataFrame('NOK','2021-03-05')
    NOK20210312call ,NOK20210312put = BuildDataFrame('NOK','2021-03-12')
    NOK20210319call ,NOK20210319put = BuildDataFrame('NOK','2021-03-19')
    NOK20210416call ,NOK20210416put = BuildDataFrame('NOK','2021-04-16')
    NOK20210618call ,NOK20210618put = BuildDataFrame('NOK','2021-06-18')
    NOK20210716call ,NOK20210716put = BuildDataFrame('NOK','2021-07-16')
    NOK20220121call ,NOK20220121put = BuildDataFrame('NOK','2022-01-21')
    NOK20230120call ,NOK20230120put = BuildDataFrame('NOK','2023-01-20')
    ArbitrageHunter([NOK20210205call, NOK20210212call, NOK20210219call, NOK20210226call, NOK20210305call, NOK20210312call, NOK20210319call, NOK20210416call, NOK20210618call, NOK20210716call, NOK20220121call, NOK20230120call])
    ArbitrageHunter([NOK20210205put, NOK20210212put, NOK20210219put, NOK20210226put, NOK20210305put, NOK20210312put, NOK20210319put, NOK20210416put, NOK20210618put, NOK20210716put, NOK20220121put, NOK20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))

    CCL20210205call ,CCL20210205put = BuildDataFrame('CCL','2021-02-05')
    CCL20210212call ,CCL20210212put = BuildDataFrame('CCL','2021-02-12')
    CCL20210219call ,CCL20210219put = BuildDataFrame('CCL','2021-02-19')
    CCL20210226call ,CCL20210226put = BuildDataFrame('CCL','2021-02-26')
    CCL20210305call ,CCL20210305put = BuildDataFrame('CCL','2021-03-05')
    CCL20210312call ,CCL20210312put = BuildDataFrame('CCL','2021-03-12')
    CCL20210319call ,CCL20210319put = BuildDataFrame('CCL','2021-03-19')
    CCL20210416call ,CCL20210416put = BuildDataFrame('CCL','2021-04-16')
    CCL20210716call ,CCL20210716put = BuildDataFrame('CCL','2021-07-16')
    CCL20220121call ,CCL20220121put = BuildDataFrame('CCL','2022-01-21')
    CCL20230120call ,CCL20230120put = BuildDataFrame('CCL','2023-01-20')
    ArbitrageHunter([CCL20210205call, CCL20210212call, CCL20210219call, CCL20210226call, CCL20210305call, CCL20210312call, CCL20210319call, CCL20210416call, CCL20210716call, CCL20220121call, CCL20230120call])
    ArbitrageHunter([CCL20210205put, CCL20210212put, CCL20210219put, CCL20210226put, CCL20210305put, CCL20210312put, CCL20210319put, CCL20210416put, CCL20210716put, CCL20220121put, CCL20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))

    SLV20210212call ,SLV20210212put = BuildDataFrame('SLV','2021-02-12')
    SLV20210219call ,SLV20210219put = BuildDataFrame('SLV','2021-02-19')
    SLV20210226call ,SLV20210226put = BuildDataFrame('SLV','2021-02-26')
    SLV20210305call ,SLV20210305put = BuildDataFrame('SLV','2021-03-05')
    SLV20210416call ,SLV20210416put = BuildDataFrame('SLV','2021-04-16')
    SLV20210630call ,SLV20210630put = BuildDataFrame('SLV','2021-06-30')
    SLV20210716call ,SLV20210716put = BuildDataFrame('SLV','2021-07-16')
    SLV20210930call ,SLV20210930put = BuildDataFrame('SLV','2021-09-30')
    SLV20211231call ,SLV20211231put = BuildDataFrame('SLV','2021-12-31')
    SLV20220121call ,SLV20220121put = BuildDataFrame('SLV','2022-01-21')
    SLV20220617call ,SLV20220617put = BuildDataFrame('SLV','2022-06-17')
    SLV20230120call ,SLV20230120put = BuildDataFrame('SLV','2023-01-20')
    ArbitrageHunter([SLV20210212call, SLV20210219call, SLV20210226call, SLV20210305call,SLV20210416call, SLV20210630call, SLV20210716call, SLV20210930call, SLV20211231call, 
    SLV20220121call, SLV20220617call, SLV20230120call])
    ArbitrageHunter([SLV20210212put, SLV20210219put, SLV20210226put, SLV20210305put,SLV20210416put, SLV20210630put, SLV20210716put, SLV20210930put, SLV20211231put, SLV20220121put, SLV20220617put, SLV20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))

    BB20210205call ,BB20210205put = BuildDataFrame('BB','2021-02-05')
    BB20210212call ,BB20210212put = BuildDataFrame('BB','2021-02-12')
    BB20210219call ,BB20210219put = BuildDataFrame('BB','2021-02-19')
    BB20210226call ,BB20210226put = BuildDataFrame('BB','2021-02-26')
    BB20210305call ,BB20210305put = BuildDataFrame('BB','2021-03-05')
    BB20210312call ,BB20210312put = BuildDataFrame('BB','2021-03-12')
    BB20210319call ,BB20210319put = BuildDataFrame('BB','2021-03-19')
    BB20210618call ,BB20210618put = BuildDataFrame('BB','2021-06-18')
    BB20210917call ,BB20210917put = BuildDataFrame('BB','2021-09-17')
    BB20220121call ,BB20220121put = BuildDataFrame('BB','2022-01-21')
    BB20230120call ,BB20230120put = BuildDataFrame('BB','2023-01-20')
    ArbitrageHunter([BB20210205call, BB20210212call, BB20210219call, BB20210226call, BB20210305call, BB20210312call, BB20210319call, BB20210618call, BB20210917call, BB20220121call, BB20230120call])
    ArbitrageHunter([BB20210205put, BB20210212put, BB20210219put, BB20210226put, BB20210305put, BB20210312put, BB20210319put, BB20210618put, BB20210917put, BB20220121put, BB20230120put])
    time.sleep(90)
    print("Operation took %s seconds ---" % (time.time() - start_time))
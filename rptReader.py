# -*- coding: utf-8 -*-
#!/usr/bin/python
"""TWSE RPT Reader
"""

import sys
import os
import multiprocessing
import multiprocessing.dummy
import settings


def OptionsDailyReader(rptFile):
    rslt = []
    
    #Get Cpu core
    coreNumbers = multiprocessing.cpu_count()

    # check python version.
    if sys.version_info.major == 2:
        import codecs
        srcFile = codecs.open(rptFile, encoding='big5')
    else:
        srcFile = open(rptFile, encoding='big5')

    datas = srcFile.readlines()

    # data[0] and data[1] is not use.
    for i in range(2):
        del datas[0]
    
    print("Map rpt and data")
    pool = multiprocessing.dummy.Pool(coreNumbers)
    optionsDailyList = pool.map(OptionsDailyFormat, datas)
    pool.close()
    pool.join()
    
    return optionsDailyList

def OptionsDailyOutput(optionsDailyList):
    path = settings.SAVE_OPTIONS_DAILY_PATH+settings.SEP+optionsDailyList[0][0]
    opDict = {}  # dictionary to save there options instrument
    
    # Re-write to become a function?
    if not os.path.isdir(path):
        os.makedirs(path)
    
    for data in optionsDailyList:
        key = tuple(data[:5])
        if not opDict.has_key(key):
            opDict.setdefault(key, [])
        opDict[key].append(data[5:8])
    
    # Output
    for key, value in opDict.iteritems():
        fn = '_'.join(key)  # filename
        try:
            print("[Output]" + fn)
            with open(path+settings.SEP+fn, 'w+b') as file:
                for instrument in value:
                    data = ' '.join(key) + ' ' + ' '.join(instrument)
                    file.write(data+'\n')
        except IOError:
            print("IOError..")
            continue
            
    return opDict

def OptionsDailyFormat(data):
    data = data.replace(' ', '').replace(',\n', '')
    return data.split(',')

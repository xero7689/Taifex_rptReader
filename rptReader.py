"""
rptReader Obj
"""

#!/usr/bin/python
import sys
import multiprocessing
import multiprocessing.dummy
import time


def RPTReader(rptFile):
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

    # using for loop:
    # for data in datas:
        # rslt.append(rptFormat(data))

    print("Map rpt and data")
    pool = multiprocessing.dummy.Pool(coreNumbers)

    rslt = pool.map(rptFormat, datas)
    pool.close()
    pool.join()

    '''
    # using map
    pool = multiprocessing.Pool()
    pool.map(rptFormat, datas)
    pool.close()
    pool.join()
    '''

    #Outputfile
    srcFile.close()
    return rslt

def rptFormat(data):
    data = data.replace(' ', '').replace(',\n', '')
    return data.split(',')


'''
class rptReader():

    def __init__(self, rptFileName):
        # check python version.
        if sys.version_info.major == 2:
            from codecs import open as open

        # open srcFileim
        with codecs.open(rptFile, encoding='big5') as srcFile:
            self.data = srcFile.readline()
'''

'''
class Comodity
'''

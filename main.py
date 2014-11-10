"""
Python rpt file reader for data from:
http://www.taifex.com.tw/chinese/3/dl_3_2_4.asp
For python2
"""
#!/usr/bin/python
import sys
import os
import time
import multiprocessing
from rptReader import RPTReader

SRC_DIR = 'srcFile'
SAVE_DIR = 'save'
WORKING_PATH = os.path.dirname(os.path.abspath('__file__'))
SOURCE_FILE_PATH = os.path.join(WORKING_PATH, SRC_DIR)
SAVE_FILE_PATH = os.path.join(WORKING_PATH, SAVE_DIR)


def get_rpt_file(folder):
    return(os.path.join(folder, f) for f in os.listdir(folder) if 'rpt' in f)


def main():
    if not os.path.isdir(SAVE_DIR):
        print("Create dir.")
        os.mkdir(SAVE_FILE_PATH)
    rptFile = get_rpt_file(SOURCE_FILE_PATH)
    '''
    start = time.time()
    for file in rptFile:
        print(file)
        RPTReader(file)
    end = time.time()
    print("for-loop Time cost: " + str(end-start))
    '''
    
    start = time.time()
    pool = multiprocessing.Pool()
    pool.map(RPTReader, rptFile)
    pool.close()
    pool.join()

    end = time.time()
    print("pool map Time cost: " + str(end-start))

if __name__ == '__main__':
    main()

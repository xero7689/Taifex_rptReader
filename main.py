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
from settings import *
from rptReader import *
from unzip import *


def get_rpt_file(folder):
    return(os.path.join(folder, f) for f in os.listdir(folder) if 'rpt' in f)

def main():
    # Unzip File
    unzipOptionsDaily()

    # Read OptionsDaily
    if not os.path.isdir(SAVE_DIR):
        print("Create dir.")
        os.mkdir(SAVE_FILE_PATH)
        
    rptFile = get_rpt_file(SOURCE_OPTIONS_DAILY_PATH)
    
    for file in rptFile:
        print('[Reading]' + str(file))
        rslt = OptionsDailyReader(file)
        OptionsDailyOutput(rslt)

if __name__ == '__main__':
    main()

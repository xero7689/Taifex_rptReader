import os
import zipfile

from setting import SEP, ZIP_OPTIONS_DAILY_PATH, SOURCE_OPTIONS_DAILY_PATH

def get_zip_file(folder):
    return(os.path.join(folder, f) for f in os.listdir(folder) if 'zip' in f)

def unzipOptionsDaily():
    
    zipList = get_zip_file(ZIP_OPTIONS_DAILY_PATH)
    
    # if directory of options daily doesn'y exist, then make dir. 
    if not os.path.isdir(SOURCE_OPTIONS_DAILY_PATH):
        os.mkdir(SOURCE_OPTIONS_DAILY_PATH)
        
    for z in zipList:
        zfile = zipfile.ZipFile(z, 'r')
        for fn in zfile.namelist():
            data = zfile.read(fn)
            output = open(SOURCE_OPTIONS_DAILY_PATH+SEP+fn, 'w+b')
            output.write(data)
            output.close()
            

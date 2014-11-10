import os

if os.name == 'nt':
    SEP = '\\\\'
elif os.name == 'posix':
    SEP = '/'

WORKING_PATH = os.path.dirname(os.path.abspath('__file__'))

OPTIONS_DAILY_DIR = 'OptionsDaily'

SRC_DIR = 'srcFile'
SOURCE_FILE_PATH = os.path.join(WORKING_PATH, SRC_DIR)
SOURCE_OPTIONS_DAILY_PATH = os.path.join(SOURCE_FILE_PATH, OPTIONS_DAILY_DIR)

SAVE_DIR = 'save'
SAVE_FILE_PATH = os.path.join(WORKING_PATH, SAVE_DIR)

ZIP_DIR = 'zipFile'
ZIP_FILE_PATH = os.path.join(WORKING_PATH, ZIP_DIR)
ZIP_OPTIONS_DAILY_PATH = os.path.join(ZIP_FILE_PATH, OPTIONS_DAILY_DIR)

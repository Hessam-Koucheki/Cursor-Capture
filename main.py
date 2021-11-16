from win32 import win32gui
from datetime import datetime
import time
from os.path import dirname
from os import makedirs

TIME = str(time.localtime().tm_year) +'_'+ str(time.localtime().tm_mon) +'_'+ str(time.localtime().tm_mday) +'_'+ str(time.localtime().tm_hour) +'_'+ str(time.localtime().tm_min)
LOG_FILE_DIR = str(dirname(__file__)) + '\\log\\'
FILE_ADDR = LOG_FILE_DIR + TIME + '.txt'
print(FILE_ADDR)
try:
    open(FILE_ADDR, 'a')
except:
    makedirs(LOG_FILE_DIR)
    
with open(FILE_ADDR, 'a') as cur_file:
    exit()
while 1:
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    print(x, y)

flags, hcursor, (x,y) = win32gui.GetCursorInfo()
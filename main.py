from win32 import win32gui
from datetime import datetime
from time import localtime
from os.path import dirname
from os import makedirs

TIME = str(localtime().tm_year) +'_'+ str(localtime().tm_mon) +'_'+ str(localtime().tm_mday) +'_'+ str(localtime().tm_hour)
LOG_FILE_DIR = str(dirname(__file__)) + '\\log\\'
FILE_ADDR = LOG_FILE_DIR + TIME + '_'
print(FILE_ADDR)
try:
    f = open(FILE_ADDR + str(localtime().tm_min) + '.txt', 'a')
    f.close()
except:
    makedirs(LOG_FILE_DIR)
    
while 1:
    cur_min = localtime().tm_min
    with open(FILE_ADDR + str(cur_min) + '.txt', 'a') as cur_file:
        if cur_min != localtime().tm_min:
            cur_min = localtime().tm_min
        flags, hcursor, (x,y) = win32gui.GetCursorInfo()
        print(x, y)
        cur_file.write(TIME+'\n')
            
flags, hcursor, (x,y) = win32gui.GetCursorInfo()
from win32 import win32gui
from datetime import datetime
import time
flags, hcursor, (x,y) = win32gui.GetCursorInfo()

# print(time.localtime().tm_year)
# print(time.localtime().tm_mon)
# print(time.localtime().tm_mday)
# print(time.localtime().tm_hour)
# print(time.localtime().tm_min)


TIME = str(time.localtime().tm_year) +'_'+ str(time.localtime().tm_mon) +'_'+ str(time.localtime().tm_mday) +'_'+ str(time.localtime().tm_hour) +'_'+ str(time.localtime().tm_min)

FILE_ADDR =  TIME + '.txt'


with open(FILE_ADDR, 'w') as cur_file:
    exit()
while 1:
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    print(x, y)

from win32 import win32gui
from time import localtime, sleep
from os.path import dirname
from os import makedirs, system
import mouse

system('cls')
TIME = str(localtime().tm_year) +'_'+ str(localtime().tm_mon) +'_'+ str(localtime().tm_mday) +'_'+ str(localtime().tm_hour)
LOG_FILE_DIR = str(dirname(__file__)) + '\\log\\'
FILE_ADDR = LOG_FILE_DIR + TIME + '_'

try:
    f = open(FILE_ADDR + str(localtime().tm_min) + '.txt', 'a')
    f.close()
except:
    makedirs(LOG_FILE_DIR)

SECOND_TO_CAPTURE = 10 # 10 MIN of recording mouse movements
SECOND_TO_WAIT = 1/2 # 0.5 SECONDs wait before capture next mouse position

# Menu
choice = 123456789
while choice != 1 and choice != 2:
    print('Enter 1: Start Mouse Recording.')
    print('Enter 2: Start Mouse Performing.')
    choice = int(input('>>> '))
    if choice != 1 and choice != 2 and choice != 123456789:
        print('Wrong Input!!', choice, type(choice))
        sleep(1)
        system('cls')

# Capturing
if choice == 1:
    system('cls')
    while 1:
        try:
            SECOND_TO_CAPTURE = int(input('How many seconds you want to Capture?\n>>> '))
        except:
            print('You should enter an integer!!')
            sleep(1)
            continue
        break
    for i in range(SECOND_TO_CAPTURE):
        cur_min = localtime().tm_min
        with open(FILE_ADDR + str(cur_min) + '.txt', 'a') as cur_file:
            flags, hcursor, (x,y) = win32gui.GetCursorInfo()
            print(x, y)
            mouse_pos =  ' ' + str(x) + ' ' + str(y)
            cur_file.write(str(localtime().tm_sec) + mouse_pos + '\n')
            sleep(1)
    print('Recording is Finished!!')

# Performing
if choice == 2:
    print('Running Mouse Movements')
    with open(FILE_ADDR + str(cur_min) + '.txt', 'r') as cur_file:
        lines = cur_file.readlines()
        for line in lines:
            t, x, y = line.split()
            print(t, x, y)
            mouse.move(x,y)
            sleep(SECOND_TO_WAIT)

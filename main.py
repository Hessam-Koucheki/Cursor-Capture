from win32 import win32gui
flags, hcursor, (x,y) = win32gui.GetCursorInfo()
while 1:
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()
    print(x, y)

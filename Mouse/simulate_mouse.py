from pprint import pprint as pp
import win32api, win32con
import time

# Mouse Control
def mouse_control(pos:tuple, click:bool=False):
    x = pos[0]
    y = pos[1]
    win32api.SetCursorPos((x,y))
    if click:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

mouse_control((1548, 218), True)

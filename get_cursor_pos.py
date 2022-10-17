import imp
from pprint import pprint as pp
import win32gui
import keyboard

print('\nGet Cursor Program active.')
print('Press Q to exit.')
print('Press G to get the mouse posistion.\n')

while True:
    try:
        if keyboard.is_pressed('q'):
            print('Exit program...')
            break
        elif keyboard.is_pressed('g'):
            pp(win32gui.GetCursorPos())
            while keyboard.is_pressed('g'):
                pass
    except:
        break

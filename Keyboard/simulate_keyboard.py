from pprint import pprint as pp
import os
import keyboard
import time

os.startfile(r'C:\Windows\System32\notepad.exe')

print('Enter Sleep')
time.sleep(2)
print('Exit Sleep')

# Keyboard Control
inputs = ['x', 'q', '8', '*', 'enter', 'tab', 'shift+a', 'ctrl+a']
for x in inputs:
    keyboard.press_and_release(x)

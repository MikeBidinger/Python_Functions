import win32gui
import re

class WindowMgr:
    
    def __init__ (self):
        self._handle = None

    # Find window by class_name
    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    # Find window by title that matches the wildcard regex
    def find_window_wildcard(self, wildcard):
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)

w = WindowMgr()
w.find_window_wildcard(".*Hello.*")
w.set_foreground()

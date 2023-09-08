import win32api
import win32gui


def set_layout_rus():
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04190419)


set_layout_rus()


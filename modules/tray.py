from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

import gc

import pystray
from modules import window

wm = window.WindowManager()

def add_tray(memory):

    def _SwitchVisibleWindow():
        if wm.IsWindowVisible(hWnd):
            wm.HideWindow(hWnd)

        else:
            wm.ShowWindow(hWnd)

    def _ShowWindow():
        wm.ShowWindow(hWnd)

    def _HideWindow():
        wm.HideWindow(hWnd)

    def _ExitMenu():
        return

    def _Terminate():

        if not wm.IsWindowVisible(hWnd):
            wm.ShowWindow(hWnd)

        memory.window.remove(hWnd)
        Tray.stop()

    hWnd = wm.GetForegroundWindow()

    if hWnd in memory.window:
        return

    else:
        memory.window.append(hWnd)


    FileName = wm.GetWindowFileName(hWnd)
    title = wm.GetWindowTitle(hWnd)
    icon = wm.GetWindowIcon(hWnd)

    menu = pystray.Menu(
        pystray.MenuItem("Show/Hide Window", _SwitchVisibleWindow, default=True, visible=False),
        pystray.MenuItem("Show Window", _ShowWindow),
        pystray.MenuItem("Hide Window", _HideWindow),
        pystray.MenuItem("Terminate", _Terminate),
        pystray.MenuItem("Exit Menu", _ExitMenu)
    )


    Tray = pystray.Icon(name=FileName, icon=icon, title=title, menu=menu)

    Tray.run()
    gc.collect()
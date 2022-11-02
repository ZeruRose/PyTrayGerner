from PIL import Image

import win32api
import win32gui
import win32ui
import win32process
import win32con


class WindowManager():

    def __init__(self):
        pass

    def SendMessage(self, hWnd, message, wparam):
        result = win32gui.SendMessage(hWnd, message, wparam)
        return result

    def ShowWindow(self, hWnd):
        win32gui.ShowWindow(hWnd, True)

    def HideWindow(self, hWnd):
        win32gui.ShowWindow(hWnd, False)

    def IsWindowVisible(self, hWnd):
        state = win32gui.IsWindowVisible(hWnd)
        return state

    def GetWindowTitle(self, hWnd):
        return win32gui.GetWindowText(hWnd)

    def GetWindowFileName(self, hWnd):
        ProcessID = win32process.GetWindowThreadProcessId(hWnd)[-1]
        hProcess = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, ProcessID)
        FileName = win32process.GetModuleFileNameEx(hProcess, None)

        win32api.CloseHandle(hProcess)

        return FileName

    def GetForegroundWindow(self):
        hWnd = win32gui.GetForegroundWindow()

        return hWnd

    def GetWindowIcon(self, hWnd):

        hIcon = self._WindowIconGetter(hWnd)

        if hIcon:

            IconInfo = win32gui.GetIconInfo(hIcon)

            BitmapObject = win32ui.CreateBitmapFromHandle(IconInfo[4])  # type: ignore # This code has no exception.
            BitmapInfo = BitmapObject.GetInfo()
            BitmapBits = BitmapObject.GetBitmapBits(True)

        else:
            BitmapBits, BitmapInfo = self._WindowExeFileIconGetter(hWnd)

        BitmapImage = Image.frombytes('RGBA', (BitmapInfo['bmWidth'], BitmapInfo['bmHeight']), BitmapBits, "raw", "BGRA")

        win32api.CloseHandle(IconInfo[3])
        win32api.CloseHandle(IconInfo[4])

        return BitmapImage


    def _WindowIconGetter(self, hWnd):

        if hicon := win32gui.SendMessage(hWnd, win32con.WM_GETICON, win32con.ICON_SMALL):
            return hicon

        if hicon := win32gui.SendMessage(hWnd, win32con.WM_GETICON, win32con.ICON_BIG):
            return hicon

        if hicon := win32gui.GetClassLong(hWnd, win32con.GCL_HICONSM):
            return hicon

        if hicon := win32gui.GetClassLong(hWnd, win32con.GCL_HICON):
            return hicon

        else:
            False


    def _WindowExeFileIconGetter(self, hWnd):
        FileName = self.GetWindowFileName(hWnd)
        icon_large, icon_small = win32gui.ExtractIconEx(FileName, 0)

        if len(icon_large):
            list[map(win32gui.DestroyIcon, icon_small+icon_large[1:])]
            icon = icon_large[0]
            icon_size = {"width": 32, "height": 32}

        elif len(icon_small):
            list[map(win32gui.DestroyIcon, icon_large+icon_small[1:])]
            icon = icon_small[0]
            icon_size = {"width": 16, "height": 16}

        else:
            return win32api.LoadIcon(0, win32con.IDI_WINLOGO)


        hDC = win32ui.CreateDCFromHandle(win32gui.GetDC(0))

        hBitmap = win32ui.CreateBitmap()
        hBitmap.CreateCompatibleBitmap(hDC, icon_size["width"], icon_size["height"])

        hDC = hDC.CreateCompatibleDC()
        hDC.SelectObject(hBitmap)
        hDC.DrawIcon((0,0), icon)

        BitmapBits = hBitmap.GetBitmapBits(True)
        BitmapInfo = hBitmap.GetInfo()


        win32gui.DestroyIcon(icon)

        return (BitmapBits, BitmapInfo)

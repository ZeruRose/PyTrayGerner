from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import traceback

import json
import keyboard
from modules import window

from modules import tray

Pool = ThreadPoolExecutor(max_workers=30)
wm = window.WindowManager()


settings = json.load(open("Settings/Keyboard.json", mode="r"))
hotkey = "+".join(settings["HotKey"])

def PostPool(memory):

    if len(memory.window) == 30:
        return

    Pool.submit(tray.add_tray, memory)

def regist(memory):

    keyboard.add_hotkey(hotkey, PostPool, [memory])
    keyboard.wait()
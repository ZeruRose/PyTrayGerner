from multiprocessing import Value
from modules import hotkey, tray, window

memory = Value("d", 1)
memory.window = []

hotkey.regist(memory)
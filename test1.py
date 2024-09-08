import keyboard
import time
import threading
import pynput
from ___Keys___ import key_list_for_pynput

keyList = ()

keyBoard = pynput.keyboard.Controller()
KEY = pynput.keyboard.Key

def Func1(key):
    try:
        if key.vk in key_list_for_pynput:
            pass
    except:
        try:
            print(f"{key}")
        except:
            print("undefined key pressed")
def Func2(key):
    try:
        print(f"{key.vk} is released")
    except:
        try:
            print(f"{key}")
        except:
            print("undefined key pressed")

keyListener = pynput.keyboard.Listener(
    on_press=Func1, on_release=Func2
)
keyListener.start()

while True:
    print(keyList)
    time.sleep(0.01)



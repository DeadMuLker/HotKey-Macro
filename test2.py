import keyboard
import time
import pynput

keyBoard = pynput.keyboard.Controller()
KEY = pynput.keyboard.Key

key_list = set([])

def Func1(event):
    if event.event_type == keyboard.KEY_DOWN:
        key_list.add(event.name)
def Func2(event):
    try:
        if event.event_type == keyboard.KEY_UP:
            key_list.remove(event.name)
    except Exception as error:
        print(error)

# keyboard.hook(callback=Func1)
# keyboard.hook(callback=Func2)

while True:
    # print(key_list)
    if keyboard.is_pressed("x"):
        keyBoard.press("x")
        time.sleep(0.01)
        keyBoard.release("x")
        time.sleep(0.01)
    time.sleep(0.01)



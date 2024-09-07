import keyboard
import time

def Func1(event):
    print(f"{event.name} is pressed")

keyboard.on_press(callback=Func1)

while True:
    time.sleep(0.01)


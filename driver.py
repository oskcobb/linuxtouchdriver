import mouse
import time
from os import system, name
import pyautogui

def wait(t):
    time.sleep(t)

def cls():
    #windows
    if name == 'nt':
        _ = system('cls')
    #mac and linux
    else:
        _ = system('clear')

cls()
while True:
    try:
        i = mouse.get_position()
        print(i)
        i1 = i
        print(i1)
        wait(0.2)
        if i == i1:
            pyautogui.mouseUp()
        else:
            pyautogui.mouseDown()
    except KeyboardInterrupt:
        cls()
        print("Exiting...")
        wait(1)
        exit()

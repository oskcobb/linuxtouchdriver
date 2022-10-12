''' 
Program by Oskar L. Cobb
written on 10/10/2022 
'''

# import libraries
import mouse
import time
from os import system, name
import pyautogui

# change time.sleep() to wait() because I kept typing it by mistake
def wait(t):
    time.sleep(t)

# setup clear screen funtion
def cls():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac and linux
    else:
        _ = system('clear')

# clear
cls()
while True:
    try:
        # check mouse possition
        i = mouse.get_position()
        # display results
        print(i)
        # duplicate values into another variable for reference
        i1 = i
        # display results
        print(i1)
        wait(0.2)
        # check if the varibles are the same
        if i == i1:
            # release left mouse button
            pyautogui.mouseUp()
        else:
            # press left mouse button
            pyautogui.mouseDown()
    # if ctrl-c is pressed, exit cleanly
    except KeyboardInterrupt:
        cls()
        print("Exiting...")
        wait(1)
        exit()

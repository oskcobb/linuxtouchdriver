# import libraries
from Xlib import display
import mouse
import pyautogui
import time
import math

# change time.sleep() to wait() because I kept typing it by mistake
def wait(t):
	time.sleep(t)

i = 5
pyautogui.FAILSAFE = False

while True:
	wait(0.5)
	# check mouse possition
	data = display.Display().screen().root.query_pointer()._data
	x = data["root_x"]
	y = data["root_y"]
	# display results
	print(x, y)
   	# check if screen is being touched
	if i == 5:
		x1 = x
		y1 = y
		wait(0.1)
		data = display.Display().screen().root.query_pointer()._data
		x = data["root_x"]
		y = data["root_y"]
		# display results
		print(x, y)
		print(x1, y1)
		# check if the mouse has moved
		if x == x1 and y == y1:
			# if it hasn't, then check if the previous possition is close to the current one
			while math.isclose(x, x1, rel_tol = 500) and math.isclose(y, y1, rel_tol = 500 ):
				# hold left mouse button down
				pyautogui.mouseDown()
			else:
				# release left mouse button
				pyautogui.mouseUp()

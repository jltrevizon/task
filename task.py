import threading
import datetime

from	 pynput.mouse import Button
from pynput.keyboard import Key
import pynput.mouse    as ms
import pynput.keyboard as kb
import time
import random
import os
import sys
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
runWhile=False
keyboard = kb.Controller()
x = 1024
y = 800
mouse = ms.Controller()

def keyPress(key, t = 1):
	keyboard.press(key)
	keyboard.release(key)
	time.sleep(t)

def altTab():
	sys=os.name
	if sys=='nt':
		print ("Is Win ")
		keyboard.press(Key.alt)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.release(Key.alt)
	else:
		print ("ALT+TAB")
		keyboard.press(Key.alt)
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		keyboard.release(Key.alt)
	time.sleep(1)


def moveMouse():
	random_x = random.randint(1, x)
	random_y = random.randint(1, y)
	mouse.position = (random_x , random_y)
	mouse.move(20, -13)
	step = random.randint(-10, 10)
	mouse.scroll(0, step)
	
def exec():
	while runWhile:
		print('each')
		keyPress(Key.right)
		moveMouse()		
		keyPress(Key.down)
		moveMouse()
		keyPress(Key.left)
		moveMouse()
		keyPress(Key.up)
		moveMouse()
		altTab()
		time.sleep(1)

def on_press(key):
    global runWhile
    if runWhile:
        # print(key)
        print ("keypress f9 to puse or f10 to terminate")
    else:
        print ("keypress f8 to start")
    if key == Key.f8 and runWhile==False:
        runWhile = True
        thread = threading.Thread(target=exec)
        thread.start()

    if key == Key.f9 and runWhile==True:
        runWhile = False
        print("TASK STOPPED", datetime.datetime.now(), '\n')
        
    if key == Key.f10:
        print("listener TERMINATED", datetime.datetime.now(), '\n')
        sys.exit() 

#--- main ---
print ("keypress f8 to start")
with kb.Listener(on_press=on_press) as listener:
    listener.join()
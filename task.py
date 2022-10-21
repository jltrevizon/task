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
#sys.stdout = open(os.devnull, "w")
#sys.stderr = open(os.devnull, "w")
runWhile=False
keyboard = kb.Controller()
x = 1024
y = 800
count=0
mouse = ms.Controller()

def keyPress(key, t = 0.5):
	keyboard.press(key)
	time.sleep(t)
	keyboard.release(key)
	time.sleep(t)

def altTab():
	sys=os.name
	keyboard.press(Key.alt)
	time.sleep(0.5)
	keyboard.press(Key.tab)
	time.sleep(0.5)
	if sys=='nt':
		print ("Is Win ")
		keyboard.release(Key.tab)
		time.sleep(0.5)
		keyboard.press(Key.tab)
		time.sleep(0.5)
	else:
		print ("ALT+TAB")
	keyboard.release(Key.tab)
	time.sleep(0.5)
	keyboard.release(Key.alt)
	time.sleep(0.5)

def nextView():
	keyboard.press(Key.ctrl)
	time.sleep(0.5)
	keyboard.press(Key.page_down )
	time.sleep(0.5)
	keyboard.release(Key.page_down)
	time.sleep(0.5)
	keyboard.release(Key.ctrl)
	time.sleep(0.5)

def previousView():
	keyboard.press(Key.ctrl)
	time.sleep(0.5)
	keyboard.press(Key.page_up)
	time.sleep(0.5)
	keyboard.release(Key.page_up)
	time.sleep(0.5)
	keyboard.release(Key.ctrl)
	time.sleep(0.5)
def moveMouse():
	random_x = random.randint(1, x)
	random_y = random.randint(1, y)
	mouse.position = (random_x , random_y)
	mouse.move(20, -13)
	step = random.randint(-10, 10)
	mouse.scroll(0, step)
	
def exec():
	while runWhile:
		global count
		count=count + 1
		keyPress(Key.right)
		moveMouse()		
		keyPress(Key.down)
		moveMouse()
		keyPress(Key.left)
		moveMouse()
		keyPress(Key.up)
		moveMouse()
		nextView()
		if count%3==0:
			altTab()
			previousView()
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
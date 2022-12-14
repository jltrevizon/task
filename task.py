import threading
import datetime
import pyautogui
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
wh = pyautogui.size() 
x = wh.width
y = wh.height
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
	moveMouseTo(random_x , random_y)
	step = random.randint(-10, 10)
	mouse.scroll(0, step)
	
def moveMouseTo(x,y,t=random.random()):
	pyautogui.moveTo(x, y, t, pyautogui.easeInQuad)     # start slow, end fast
	pyautogui.moveTo(x, y, t, pyautogui.easeOutQuad)    # start fast, end slow
	pyautogui.moveTo(x, y, t, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
	pyautogui.moveTo(x, y, t, pyautogui.easeInBounce)   # bounce at the end
	pyautogui.moveTo(x, y, t, pyautogui.easeInElastic)

def exec():
	while runWhile:
		global count
		count=count + 1
		r1 = random.random()
		for j in range(1, random.randint(1, 10)):
			if (r1> random.random()):
				keyPress(Key.right)
				moveMouse()		
				keyPress(Key.down)
				moveMouse()
				keyPress(Key.left)
				moveMouse()
				keyPress(Key.up)
				moveMouse()
		if (random.random()>random.random()):
			keyPress(Key.page_up,0)
			keyPress(Key.page_down,0)
			keyPress(Key.scroll_lock,0)
			keyPress(Key.shift,0)
			keyPress(Key.ctrl,0)
			keyPress(Key.alt,0)
		if (random.random()<random.random()):
			keyPress(Key.alt_gr,0)
			keyPress(Key.home,0)
			keyPress(Key.end,0)
			keyPress(Key.insert,0)
			keyPress(Key.page_up,0)
			keyPress(Key.page_down,0)
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
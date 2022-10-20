# instalar :  
#>pip install pynput
#>pip install pykeyboard
# Ejecutar 
#>python task.py

from pynput.mouse import Button
from pynput.keyboard import Key
import pynput.mouse    as ms
import pynput.keyboard as kb
import time
import random
import os
import sys
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
						 
keyboard = kb.Controller()
x = 1024
y = 800
print("Width =", x)
print("Height =", y)
mouse = ms.Controller()
print ("Init position: " + str(mouse.position))
while 0==0:
	for i in range(1,10):
		keyboard.press(Key.right)
		keyboard.release(Key.right)
		print ("Tecla right")
		time.sleep(0.1)
		keyboard.press(Key.down)
		keyboard.release(Key.down)
		print ("Tecla down")
		time.sleep(0.1)
		keyboard.press(Key.left)
		keyboard.release(Key.left)
		print ("Tecla left")
		time.sleep(0.1)
		keyboard.press(Key.up)
		keyboard.release(Key.up)
		print ("Tecla up")
		time.sleep(0.1)
		for j in range(1,10):
			print ("Current position: " + str(i) + "," +str(j)+ " = " + str(mouse.position))
			random_x = random.randint(1, x)
			random_y = random.randint(1, y)
			mouse.position = (random_x , random_y)
			mouse.move(20, -13)
			print ("Final position: " + str(mouse.position))
			time.sleep(1)
			step = random.randint(-10, 10)
			mouse.scroll(0, step)
			time.sleep(1)
		print ("ALT+TAB")
		keyboard.press(Key.alt) #Alt
		time.sleep(1)
		keyboard.press(Key.tab) #Tab
		time.sleep(1)
		keyboard.release(Key.tab) #~Tab
		time.sleep(0.5)	
		if os.name == 'nt':
			print ("Is Win ")
			keyboard.press(Key.tab) #Tab
			time.sleep(1)
			keyboard.release(Key.tab) #~Tab
			time.sleep(0.5)		
		keyboard.release(Key.alt) #~Alt
	keyboard.press(Key.right)
	keyboard.release(Key.right)
	print ("Tecla right")
	time.sleep(0.1)
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	print ("Tecla down")
	time.sleep(0.1)
	keyboard.press(Key.left)
	keyboard.release(Key.left)
	print ("Tecla left")
	time.sleep(0.1)
	keyboard.press(Key.up)
	keyboard.release(Key.up)
	print ("Tecla up")
	print ("Duerme 3 minutos...")
	time.sleep(180)		
		
# Click the left button
#mouse.click(Button.left, 1)
# Click the right button
#mouse.click(Button.right, 1)
# Click the middle button
#mouse.click(Button.middle, 1)
# Double click the left button
#mouse.click(Button.left, 2)
# Click the left button ten times
#mouse.click(Button.left, 10)
#mouse.press(Button.left)
#mouse.release(Button.left)
# Scroll up two steps
#mouse.scroll(0, 2)
# Scroll right five steps
#mouse.scroll(5, 0)
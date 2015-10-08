#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Joystick
	'''
	Initialize the Joystick module with SunFounder_PiPlus.Joystick()
	'''
	Joystick = Joystick()

def main():
	while True:
		'''
		get_status()
		returns a status value in UP, DOWN, LEFT, RIGHT, HOME and PRESSED
		Recognize it like this:
		'''
		status =  Joystick.get_status()
		if status == UP:
			print 'up'
		if status == DOWN:
			print 'down'
		if status == LEFT:
			print 'left'
		if status == RIGHT:
			print 'right'
		if status == HOME:
			print 'home'
		if status == PRESSED:
			print 'Button pressed'

		'''
		read()
		A function to read all the 3 pins of Joystick. It returns 3 values:
		x value, y value and button value. The value will be like this:
		'''
		print 'X = %d, Y = %d, Button = %d.'% Joystick.read()
				
		
		time.sleep(0.2)

def destroy():
	Joystick.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

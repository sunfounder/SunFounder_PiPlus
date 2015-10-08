#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Buttons
	'''
	Initialize the Buttons module with SunFounder_PiPlus.Buttons(port='A')
	Set the port to A or B, depending on which port you plug the module in.
	By default, port='A'.
	'''
	Buttons = Buttons(port='B')
	'''
	Set callbacks for falling, rising or both edge detections
	add_event_detect(up_falling=None, left_falling=None, down_falling=None, right_falling=None, 
					 up_rising=None,	left_rising=None,  down_rising=None,  right_rising=None, 
					 up_both=None, 	left_both=None,    down_both=None,    right_both=None)
	Choose the Button you need, what kind of edge it would be and what callback
	function's name it is. If you need no button, just leave it empty. 
	DO NOT DEFINE TWO EDGE DETECTION EVENTS FOR ONE BUTTON!
	Like this:
	'''
	Buttons.add_event_detect(up_falling=up, left_rising=left, down_both=down)
	

def main():
	while True:
		pass


# Add callback function for each button
def up(chn):
	print 'up falling!'
	
def left(chn):
	print 'left rising'

def down(chn):
	tmp = GPIO.input(Buttons.DOWN)
	if tmp == 0:
		print 'down falling!'
	elif tmp == 1:
		print 'down rising'

def right(chn):
	pass

def destroy():
	Buttons.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RE
	'''
	Initialize the Rotary Encoder module with SunFounder_PiPlus.Rotary_Encoder(port='A')
	Set the port to A or B, depending on which port you plug the module in.
	By default, port='A'.
	'''
	RE = Rotary_Encoder(port='B')
	
	'''
	Set callbacks for falling, rising or both edge detections.
	GPIO.add_event_detect(Pin, Rising/Falling, callback)
	Change Raise/Falling to 'GPIO.RISING' to detect rising, 
	Change Raise/Falling to 'GPIO.FALlING' to detect falling, 
	Change Raise/Falling to 'GPIO.BOTH' to detect both rising and falling.
	'''
	GPIO.add_event_detect(RE.BTN, GPIO.FALLING, callback=clean)

'''
Create a callback function
'''
def clean(chn):
	global init_flag
	init_flag=1

def main():
	global init_flag
	count = 0
	init_flag = 0
	tmp = 0
	while True:
		if init_flag == 1:
			count = 0
			init_flag = 0
		
		'''
		rotary_deal(_value, step=1): _value changes with the Rotary Encoder spinned - 
		clockwise, add 1; counterclockwise, minus 1. 
		step defines how much to be added/subtracted 
		for one step spinned of the Rotary Encoder 
		'''
		count = RE.rotary_deal(count, step=2)
		if tmp != count:
			print count
			tmp = count

def destroy():
	RE.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

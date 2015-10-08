#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Ring
	'''
	Initialize the LED Ring module with SunFounder_PiPlus.LED_Ring(port='A')
	Set the port to A or B, depending on which port you plug the module in.
	By default, port='A'.
	'''
	Ring = LED_Ring(port='a')
	
def main():
	while True:
		''' 
		Breathing light function: breath(dt=0.03), 
		dt is short for delay time; by default it is 0.03.
		'''
		for i in range(4):
			Ring.breath(dt=0.01)
		
		'''
		Spin function: spin(ring, w=0, dt=0.2)
		w is for wise. w=0: clockwise; w=1: anticlockwise
		dt for delay time. By default w and dt are 0.03.
		SINGLE, STAR and TAIL are three pre-set lists.
		You can make your own list as: Mylist = [0, 60, 0, 60, 60, 60, 0, 60]
		'''
		ring = list(Ring.SINGLE())
		for i in range(16):	# 8 for a circle, 16 for two
			Ring.spin(ring, dt=0.1)
		
		ring = list(Ring.STAR())	
		for i in range(16):
			Ring.spin(ring, dt=0.3)
			
		ring = list(Ring.ARC())
		for i in range(16):
			Ring.spin(ring, w=1)
		
		'''
		Meter function: LED_meter(_value, brightness=40)
		_value must be within [0, 255].
		Brightness affects all LED. By default it is 40.
		'''
		for i in range(256):
			Ring.meter(i, brightness=10)
			print i
			time.sleep(0.05)
		for i in range(256):
			Ring.meter(255-i, brightness = 80)
			print 255-i
			time.sleep(0.05)
		

def destroy():
	Ring.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

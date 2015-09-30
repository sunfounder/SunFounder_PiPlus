#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RGB, SP
	RGB = RGB_LED(port='B')
	SP = Slide_Potentiometers()

def main():
	while True:
		R, G, B = SP.get_value(1, 2, 3)
		print 'R = %d, G = %d, B = %d' % (R, G, B)
		RGB.rgb(R, G, B)

def destroy():
	RGB.destroy()
	SP.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

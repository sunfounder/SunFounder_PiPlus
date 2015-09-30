#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RGB
	'''
	initial the sample_sample module with PiPlus.Buttons(port='A')
	Set port to A or B, accoring to the port you plug the module in.
	Leave empty for default setting port='A'
	'''
	RGB = RGB_LED(port='A')

def main():
	while True:
		R = random.randint(0, 255)
		G = random.randint(0, 255)
		B = random.randint(0, 255)
		RGB.breath(R, G, B)
		print 'R = %d, G = %d, B = %d' % (R, G, B)

def destroy():
	RGB.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

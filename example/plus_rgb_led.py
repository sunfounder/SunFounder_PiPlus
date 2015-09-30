#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RGB
	'''
	initial the RGB LED module with SunFounder_PiPlus.RGB_LED(port='A')
	Set port to A or B, accoring to the port you plug the module in.
	Leave empty for default setting port='A'
	'''
	RGB = RGB_LED(port='B')

def main():
	while True:
		'''
		off() to turn off the RGB.
		'''
		RGB.off()
		
		'''
		rgb(Red_value, Green_value, Blue_value):
		This is a function to turn on the RGB 
		in specific RGB value, all value range from 0 to 255
		'''
		RGB.rgb(255, 0, 0)
		time.sleep(1)
		RGB.rgb(0, 255, 0)
		time.sleep(1)
		RGB.rgb(0, 0, 255)
		time.sleep(1)
		RGB.rgb(255, 255, 255)
		time.sleep(1)
		
		RGB.rgb(100, 180, 255)
		time.sleep(1)
		RGB.rgb(200, 100, 255)
		time.sleep(1)
		RGB.rgb(255, 0, 120)
		time.sleep(1)
		
		'''
		breath(Red_value, Green_value, Blue_value, dt=0.01): 
		This is a function to let the RGB breathe in specific RGB value,
		dt for delta time. Leave empty for default setting 0.01s
		RGB value range from 0 to 255
		'''
		RGB.breath(255, 0, 0)
		RGB.breath(0, 255, 0)
		RGB.breath(0, 0, 255)
		
		RGB.breath(0, 255, 255)
		RGB.breath(255, 0, 255)
		RGB.breath(255, 255, 0)
		
		'''
		hsb(Hue_value, _s=1, _b=1):
		This is a function to specific color in HSB.
		Hue_value range from 0 to 360
		_s and _b range from 0.00 to 1. Leave empty for default setting 1
		'''
		for i in range(360):
			RGB.hsb(i)
			time.sleep(0.1)
		
		for i in range(360):
			RGB.hsb(i, _b=0.7)
			time.sleep(0.1)
	
def destroy():
	RGB.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

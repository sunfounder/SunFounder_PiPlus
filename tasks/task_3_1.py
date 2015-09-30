#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Bar, PR
	Bar = LED_Bar_Graph(port='B')
	PR = Photoresistor()

def main():
	while True:
		temp = PR.brightness()
		print 'corrent light value =', temp
		Bar.meter(temp)

def destroy():
	Bar.destroy()
	PR.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

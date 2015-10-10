#!/usr/bin/env python
from PiPlus import *

def setup():
	global ADC
	'''
	initial the PCF8591 module with PiPlus.PCF8591()
	'''
	ADC = PCF8591()

def main():
	count = 0
	updown = 1
	while True:
		if count == 255:
			updown = 0
		if count == 0:
			updown = 1
		if updown == 1:
			count += 1
		if updown == 0:
			count -= 1
		ain0, ain1, ain2, ain3 = ADC.read_all()
		print 'AIN0 = %d\nAIN1 = %d\nAIN2 = %d\nAIN3 = %d\nAOUT = %d\n' % (ain0, ain1, ain2, ain3, count)
		
		ADC.write(count)
		time.sleep(0.05)

def destroy():
	ADC.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

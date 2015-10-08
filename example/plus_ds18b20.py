#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global TEMP
	'''
	Initialize the DS18B20 module with SunFounder_PiPlus.DS18B20()
	'''
	TEMP = DS18B20()

def main():
	while True:
		'''
		DS18B20.read(unit)
		This function reads the temperature value from DS18B20.
		Set the unit to DS18B20.C for Celsius degree
		Set the unit to DS18B20.F for Fahrenheit degree
		'''
		temp_c = TEMP.get_temperature()	# By default, it is TEMP.C.
		temp_f = TEMP.get_temperature(TEMP.F)
		print 'temperature =', temp_f, 'F'
		print 'temperature =', temp_c, 'C'
		time.sleep(0.2)

def destroy():
	TEMP.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

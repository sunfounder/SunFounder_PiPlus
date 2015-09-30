#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global TEMP
	'''
	initial the DS18B20 module with SunFounder_PiPlus.DS18B20()
	'''
	TEMP = DS18B20()

def main():
	while True:
		'''
		DS18B20.read(unit)
		This Function reads the temperature from DS18B20.
		set unit to DS18B20.C for celsius degree
		set unit to DS18B20.F for fahrenheit degree
		'''
		temp_c = TEMP.get_temperature()	# Leave empty for default setting TEMP.C
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

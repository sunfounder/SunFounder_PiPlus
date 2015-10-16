#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global TEMP, LCD, TIME
	TEMP = DS18B20()
	LCD = LCD1602()
	TIME = DS1307()

def main():
	date_tmp = ''
	time_tmp = ''
	temp_tmp = 0
	while True:
		date, time = TIME.get_split_datetime()
		temp = TEMP.get_temperature()
		print date, time, temp
		if date_tmp != date:
			LCD.write(0, 0, date)
			date_tmp = date
		if time_tmp != time:
			LCD.write(0, 1, time)
			temp_tmp = time
		if temp_tmp != temp:
			LCD.write(10, 1, '%2.2fC' % temp)
			temp_tmp = temp

def destroy():
	LCD.destroy()
	TIME.destroy()
	TEMP.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global DT
	'''
	initial the DS1307 module with SunFounder_PiPlus.DS1307(clockmode)
	set clockmode to HOUR12 for 12-hour clock, 
	set clockmode to HOUR24 for 24-hour clock, 
	'''
	DT = DS1307(HOUR12)

def main():
	while True:
		'''
		get_datetime() return the output of 'hwclock -r' command
		'''
		datetime = DT.get_datetime()
		print datetime
		'''
		get_split_datetime(), get date, time seperatelyj
		'''
		#date, time = DT.get_split_datetime()
		#print 'date:', date
		#print 'time:', time

def destroy():
	DT.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

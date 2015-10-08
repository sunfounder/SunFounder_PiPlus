#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global DT
	'''
	Initialize the DS1307 module with SunFounder_PiPlus.DS1307(clockmode)
	Set clockmode to HOUR12 for 12-hour clock, 
	Set clockmode to HOUR24 for 24-hour clock, 
	'''
	DT = DS1307(HOUR12)

def main():
	while True:
		'''
		get_datetime() returns the output of 'hwclock -r' command
		'''
		datetime = DT.get_datetime()
		print datetime
		'''
		get_split_datetime() to get and display date and time separately
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

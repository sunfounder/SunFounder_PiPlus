#!/usr/bin/env python
from SunFounder_PiPlus import *

import PiPlus
import time
def setup():
	global Buzzer
	'''
	initial the Buzzer module with SunFounder_PiPlus.Buzzer(port='A')
	Set port to A or B, accoring to the port you plug the module in.
	Leave empty for default setting port='A'
	'''
	Buzzer = Buzzer(port='B')

def main():
	while True:
		print 'on'
		# Buzzer.on() to turn on the buzzer
		Buzzer.on()
		time.sleep(1)
		
		print 'off'
		# Buzzer.off() to turn off the buzzer
		Buzzer.off()
		time.sleep(1)
		
		print 'beep'
		# Buzzer.beep(dt, times) to beep the buzzer
		# dt for delta time.
		Buzzer.beep(0.5, times=4)
	
def destroy():
	Buzzer.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

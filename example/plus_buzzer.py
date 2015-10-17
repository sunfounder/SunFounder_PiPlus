#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Buzzer
	'''
	Initialize the Buzzer module with SunFounder_PiPlus.Buzzer(port='A')
	Set the port to A or B, depending on which port you plug the module in.
	By default, port='A'.
	'''
	Buzzer = Buzzer(port='B')

def main():
	while True:
		'''
		print 'on'
		# on() to turn on the buzzer
		Buzzer.on()
		time.sleep(1)
		
		print 'off'
		# off() to turn off the buzzer
		Buzzer.off()
		time.sleep(1)
		
		print 'beep'
		# beep(dt, times) to beep the buzzer
		# dt for delay time.
		Buzzer.beep(0.5, times=4)
		'''
		
		print 'Morse code'
		# morsecode(string, speed=FAST) to convert your strings
		# to a Morse code and play it with the buzzer.
		# The argument speed could be set to SLOW or FAST.
		# By default it is FAST.
		Buzzer.morsecode('sms')
		time.sleep(1)

def destroy():
	Buzzer.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

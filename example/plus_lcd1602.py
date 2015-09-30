#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global LCD
	'''
	initial the LCD1602 module with SunFounder_PiPlus.LCD1602(BACKGROUND_LIGHT=1, ADDRESS=0x27)
	Set ADDRESS to 0x20~0x27, accoring to the address you set onthe module(see more at www.sunfounder.com).
	Set BACKGROUND_LIGHT to 0 or 1 to turn off or turn on the background light. 
	Leave empty for default setting BACKGROUND_LIGHT=1/ADDRESS=0x27
	'''
	LCD = LCD1602(BACKGROUND_LIGHT=1)

def main():
	'''
	Use write(position, row, string) to write words at specific location
	position is for position in a row. from 0 to 15
	row form 0 to 1
	'''
	LCD.write(0, 0, 'Greetings!!')
	LCD.write(1, 1, 'from SunFounder')
	time.sleep(5)
	
	'''
	Use clear() to clear the whole screen up
	'''
	LCD.clear()

	row0 = 'Thanks for'
	row1 = 'choosing PiPlus'
	LCD.write(3, 0, row0)
	LCD.write(1, 1, row1)
	while True:
		pass

def destroy():
	LCD.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

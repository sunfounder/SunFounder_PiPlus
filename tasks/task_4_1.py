#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RGB, SP, LCD
	RGB = RGB_LED(port='B')
	SP = Slide_Potentiometers()
	LCD = LCD1602()

def main():
	while True:
		R, G, B = SP.get_value(1, 2, 3)
		print 'R = %d, G = %d, B = %d' % (R, G, B)
		RGB.rgb(R, G, B)
		value = (R << 16) + (G << 8) + B
		hex_value = '%X' % value
		for i in range(1, 6):
			if value < 16**i:
				hex_value = '0'+hex_value
		print value, hex_value
		hex_value = 'RGB: 0x' + hex_value
		LCD.write(0, 0, hex_value)

def destroy():
	RGB.destroy()
	SP.destroy()
	LCD.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

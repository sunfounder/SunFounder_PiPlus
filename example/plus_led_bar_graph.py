#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Bar
	'''
	Initialize the LED Bar Graph module with SunFounder_PiPlus.LED_Bar_Graph(port='A')
	Set the port to A or B, depending on which port you plug the module in.
	By default, port='A'.
	'''
	Bar = LED_Bar_Graph(port='B')

def main():
	while True:
		'''
		meter(value) is a meter and the value ranges from 0 to 255.
		'''
		
		for x in range(255):
			Bar.meter(x)
			print 'x =', x
			time.sleep(0.01)
		
		'''
		pulse(value) is also a meter, but it defines that when the LEDs all go out 
		to the middle one, the value is 0; when the value increases, the LEDs lights up 
		from the middle to two opposite directions.
		value range from 0 to 255
		'''
		
		for x in range(628):
			y = abs(math.sin(x/100.0)*250)
			Bar.pulse(y)
			print 'x = %2f, y = %d' %(x/100.00, y)
			time.sleep(0.005)
		
	
def destroy():
	Bar.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

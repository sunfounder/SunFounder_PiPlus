#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Bar
	'''
	initial the LED Bar Graph module with SunFounder_PiPlus.LED_Bar_Graph(port='A')
	Set port to A or B, accoring to the port you plug the module in.
	Leave empty for default setting port='A'
	'''
	Bar = LED_Bar_Graph(port='B')

def main():
	while True:
		'''
		meter(value) is a meter, value range from 0 to 255.
		'''
		
		for x in range(255):
			Bar.meter(x)
			print 'x =', x
			time.sleep(0.01)
		
		'''
		pulse(value) is also a meter, but put 0 is in the middle.
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

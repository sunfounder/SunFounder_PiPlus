#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Bar, RE, status
	Bar = LED_Bar_Graph(port='A')
	RE = Rotary_Encoder(port='B')
	RE.add_event_detect(btn_rising = btn)
	status = False

def btn(chn):
	global status
	status = not status
	print status
	
def main():
	global status
	
	value = 0
	tmp = 0
	
	while True:
		if status != False:
			value = RE.rotary_deal(value, step=2)
			if value > 255:
				value = 255
			if value < 0:
				value = 0
			
			if tmp != value:
				print value
				tmp = value
			Bar.meter(value)
		else:
			Bar.off()

def destroy():
	RE.destroy()
	Bar.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

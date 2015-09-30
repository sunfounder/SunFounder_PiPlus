#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global RE
	'''
	initial the Buttons module with SunFounder_PiPlus.Buttons(port='A')
	Set port to A or B, accoring to the port you plug the module in.
	Leave empty for default setting port='A'
	'''
	RE = Rotary_Encoder(port='B')
	
	'''
	Set callbacks for falling, rising or both edge detect
	GPIO.add_event_detect(Pin, Rising/Falling, callback)
	Change Raise/Falling to 'GPIO.RISING' to detect rising, 
	Change Raise/Falling to 'GPIO.FALlING' to detect falling, 
	Change Raise/Falling to 'GPIO.BOTH' to detect both rising and falling,
	'''
	GPIO.add_event_detect(RE.BTN, GPIO.FALLING, callback=clean)

'''
Creat a callback Fuction
chn is for the callback channel from pressing the Rotary Encoder
'''
def clean(chn):
	global init_flag
	init_flag=1

def main():
	global init_flag
	count = 0
	init_flag = 0
	tmp = 0
	while True:
		if init_flag == 1:
			count = 0
			init_flag = 0
		
		'''
		rotary_deal(_value, step=1) changes _value by spining the Rotary Encoder
		clock-wise to add 1, anti clock-wise to minus 1
		step is for adding how much by spining one step of the Rotary Encoder 
		'''
		count = RE.rotary_deal(count, step=2)
		if tmp != count:
			print count
			tmp = count

def destroy():
	RE.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

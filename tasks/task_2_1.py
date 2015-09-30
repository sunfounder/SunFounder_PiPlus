#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Ring, Buttons, speed, wise, step, speed_max, speed_min
	Ring = LED_Ring(port='A')
	Buttons = Buttons(port='B')
#	Buzzer = Buzzer(port='B')
	Buttons.add_event_detect(btn1_falling=btn1, btn2_falling=btn2, btn3_falling=btn3, btn4_falling=btn4)
	speed = 8
	wise = 0
	step = 0.3
	speed_max = 150
	speed_min = 0.05

def btn1(chn):
	global speed, step, speed_max
	speed += step*speed
	if speed > speed_max:
		speed = speed_max
	print '\nspeed :', speed
	
def btn3(chn):
	global speed, step, speed_min
	speed -= step*speed
	if speed < speed_min:
		speed = speed_min
	print '\nspeed :', speed
	
def btn2(chn):
	global wise
	wise = 1
	print '\nClockwise spining'
	
def btn4(chn):
	global wise
	wise = 0
	print '\nAnti-clockwise spining'

def main():
	global speed, wise
	arc = Ring.ARC()
	while True:
		delaytime=1.0/speed
		Ring.spin(arc, w=wise, dt=delaytime)

def destroy():
	Ring.destroy()
	Buttons.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

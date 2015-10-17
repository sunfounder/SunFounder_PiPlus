#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Ring, Buttons, speed, wise, step, speed_max, speed_min
	Ring = LED_Ring(port='A')
	Buttons = Buttons(port='B')
#	Buzzer = Buzzer(port='B')
	Buttons.add_event_detect(up_falling=up, left_falling=left, down_falling=down, right_falling=right)
	speed = 8
	wise = 0
	step = 0.3
	speed_max = 150
	speed_min = 0.05

def up(chn):
	global speed, step, speed_max
	speed += step*speed
	if speed > speed_max:
		speed = speed_max
	print '\nspeed :', speed
	
def down(chn):
	global speed, step, speed_min
	speed -= step*speed
	if speed < speed_min:
		speed = speed_min
	print '\nspeed :', speed
	
def left(chn):
	global wise
	wise = 1
	print '\nClockwise spining'
	
def right(chn):
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

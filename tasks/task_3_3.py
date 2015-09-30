#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global Joystick, Ring
	Ring = LED_Ring(port='B')
	Joystick = Joystick()

def main():
	ring = Ring.ARC()
	while True:
		speed = 0.0
		x, y, btn = Joystick.read()
		status = Joystick.get_status()
		if y < 118:
			speed = abs(118-y)
			speed = 118-speed
			speed = Map(speed, 0, 120, 0.0, 20.0)
			wise = 0
		elif y > 138:
			speed = y - 138
			speed = 118-speed
			speed = Map(speed, 0, 120, 0.0, 20.0)
			wise = 1
		else:
			wise = 0
			speed = 0
		dt = speed/10
		print 'Speed =', speed
		print dt, y
		ring = Ring.spin(ring, w = wise, dt = dt)

def destroy():
	Joystick.destroy()
	Ring.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

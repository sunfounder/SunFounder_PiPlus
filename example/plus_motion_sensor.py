#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global MOTION
	'''
	initial the Plus Motion Sensor module with SunFounder_PiPlus.Motion_Sensor()
	No argument needed.
	'''
	MOTION = Motion_Sensor()

def main():
	while True:
		accel_x, accel_y, accel_z = MOTION.get_accel()
		gyro_x, gyro_y, gyro_z = MOTION.get_gyro()
		scaled_accel_x, scaled_accel_y, scaled_accel_z = MOTION.get_scaled_accel()
		scaled_gyro_x,  scaled_gyro_y, scaled_gyro_z = MOTION.get_scaled_gyro()
		rotation_x, rotation_y = MOTION.get_rotation()
		temperature = MOTION.get_temp()
		
		print 'X accel :', accel_x, ' scaled :', scaled_accel_x
		print 'Y accel :', accel_y, ' scaled :', scaled_accel_y
		print 'Z accel :', accel_z, ' scaled :', scaled_accel_z
		print ''
		print 'X gyro :', gyro_x, ' scaled :', scaled_gyro_x
		print 'Y gyro :', gyro_y, ' scaled :', scaled_gyro_y
		print 'Z gyro :', gyro_z, ' scaled :', scaled_gyro_z
		print ''
		print 'X rotation :', rotation_x
		print 'Y rotation :', rotation_y
		print ''
		print 'Temperature =', temperature
		print ''
		time.sleep(0.5)
		
def destroy():
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

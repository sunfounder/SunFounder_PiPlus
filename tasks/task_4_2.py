#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global MOTION, LCD, BTN, status
	MOTION = Motion_Sensor()
	LCD = LCD1602()
	BTN = Buttons(port='B')
	
	BTN.add_event_detect(up_falling=up, down_falling=down)
	
	status = 0

def up(chn):
	global status
	status += 1
	if status > 3:
		status = 0
		
def down(chn):
	global status
	status -= 1
	if status < 0:
		status = 3

def main():
	while True:
		if status == 0:
			scaled_accel_x, scaled_accel_y, scaled_accel_z = MOTION.get_scaled_accel()
			print 'X accel scaled :', scaled_accel_x
			print 'Y accel scaled :', scaled_accel_y
			print 'Z accel scaled :', scaled_accel_z
			print ''
			LCD.write(0, 0, 'Accel   ')
			LCD.write(8, 0, 'X:%.2f ' % scaled_accel_x)
			LCD.write(0, 1, 'Y:%.2f ' % scaled_accel_y)
			LCD.write(8, 1, 'Z:%.2f ' % scaled_accel_z)
		
		if status == 1:
			scaled_gyro_x,  scaled_gyro_y, scaled_gyro_z = MOTION.get_scaled_gyro()
			print 'X gyro scaled :', scaled_gyro_x
			print 'Y gyro scaled :', scaled_gyro_y
			print 'Z gyro scaled :', scaled_gyro_z
			print ''
			LCD.write(0, 0, 'Gyro    ')
			LCD.write(8, 0, 'X:%.2f ' % scaled_gyro_x)
			LCD.write(0, 1, 'Y:%.2f ' % scaled_gyro_y)
			LCD.write(8, 1, 'Z:%.2f ' % scaled_gyro_z)

		if status == 2:
			rotation_x, rotation_y = MOTION.get_rotation()
			print 'X rotation :', rotation_x
			print 'Y rotation :', rotation_y
			print ''
			LCD.write(0, 0, 'Rotation        ')
			LCD.write(0, 1, 'X:%.2f ' % rotation_x)
			LCD.write(8, 1, 'Y:%.2f ' % rotation_y)
		
		if status == 3:
			temperature = MOTION.get_temp()
			print 'Temperature =', temperature
			print ''
			LCD.write(0, 0, 'Temperature     ')
			LCD.write(0, 1, ' %.2f`C        ' % temperature)
		
		time.sleep(0.5)
		
def destroy():
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

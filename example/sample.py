#!/usr/bin/env python

# Import SunFounder_PiPlus
from SunFounder_PiPlus import *

# Define a setup() function
def setup():
	# Define global modules' names and other necessary variables
	global Btn, Buzz, RGB, color
	
	# Initialize your modules
	Btn = Buttons(port='B')
	Buzz = Buzzer(port='A')
	RGB = RGB_LED(port='A')
	
	# Other setup
	Btn.add_event_detect(up_both=red,left_both=green, down_both=blue, right_both=beep)
	color = [0, 0, 0]
	

# Define a main function
def main():
	# Main thing your script does
	while True:
		pass		# do nothing
		
# Define a destroy function to release resource of GPIO etc.
def destroy():
	# Add all destroy function for all Plus modules
	Btn.destroy()
	Buzz.destroy()
	RGB.destroy()

	# Clean up GPIOs MUST be at the last line in destroy function
	GPIO.cleanup()

# Other functions if necessary 
def red(chn): 
	if GPIO.input(Btn.UP) == 0:
		color[0] = 255
		RGB.rgb(color[0], color[1], color[2])
	if GPIO.input(Btn.UP) == 1:
		color[0] = 0
		RGB.rgb(color[0], color[1], color[2])

def green(chn): 
	if GPIO.input(Btn.LEFT) == 0:
		color[1] = 255
		RGB.rgb(color[0], color[1], color[2])
	if GPIO.input(Btn.LEFT) == 1:
		color[1] = 0
		RGB.rgb(color[0], color[1], color[2])

def blue(chn): 
	if GPIO.input(Btn.DOWN) == 0:
		color[2] = 255
		RGB.rgb(color[0], color[1], color[2])
	if GPIO.input(Btn.DOWN) == 1:
		color[2] = 0
		RGB.rgb(color[0], color[1], color[2])

def beep(chn): 
	if GPIO.input(Btn.RIGHT) == 0:
		Buzz.on()
	if GPIO.input(Btn.RIGHT) == 1:
		Buzz.off()

# if-main function to control the 3 functions
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

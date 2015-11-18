SunFounder PiPlus for Raspberry Pi
=======================

SunFounder PiPlus is a package for the SunFounder PiPlus Kit.

The PiPlus Kit is a kit with 14 modules, and uses no wires (not wireless) 
since it's developed based on a modulization concept. 
This package is to use PiPlus in a easy and funny way.

To use this package, first you'd better have a set of PiPlus.

Then, you need to import the package before next step, better like this:

	from SunFounder_PiPlus import *

Define the setup() function including all the classes of the module you need:
	
	def setup():
		global Buzz
		Buzz = Buzzer(port='A')

Next, define a main() functon including the pre-defined functions you need:
	
	def main():
		while True:
			Buzz.morsecode("sms")

Finally, before you run the app, define a destory() function, and an "if-main" 
funtion:
	
	def destroy():
		Buzz.destroy()
		GPIO.cleanup()

	if __name__ == "__main__":
		try:
			setup()
			main()
		except KeyboardInterrupt:
			destroy()

Save it in your favorite name, like mine buzz.py. Then, you can run the app with the command:

sudo python buzz.py

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog here is not
a good idea; but a simple "What's New" section for the most recent version
may be appropriate.

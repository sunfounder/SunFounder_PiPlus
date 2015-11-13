SunFounder PiPlus for RPi
=======================

SunFounder_PiPlus is a Package for SunFounder PiPlus Kit.

PiPlus Kit is a kit with 14 modules, and with no wire(not wireless) and modulize
concept. This package is to use PiPlus in a easy and funny way.

To use this package, First you need a set of PiPlus, would be better.

Second, to use this package, you need to import the package, better like this:

	from SunFounder_PiPlus import *

Third, define setup() function include all the class of the module you need:
	
	def setup():
		global Buzz
		Buzz = Buzzer(port='A')

Forth, define a main() functon include the pre-defined functions you need:
	
	def main():
		while True:
			Buzz.morsecode("sms")

Finally, before you run the app, define a destory function, and an "if-main" 
funtion to run the app:
	
	def destroy():
		Buzz.destroy()
		GPIO.cleanup()

	if __name__ == "__main__":
		try:
			setup()
			main()
		except KeyboardInterrupt:
			destroy()

Save it in your favorite name like buzz.py. Then, you can run the app with command:

sudo python buzz.py

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not
a good idea, although a simple "What's New" section for the most recent version
may be appropriate.

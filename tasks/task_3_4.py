#!/usr/bin/env python
from SunFounder_PiPlus import *

def setup():
	global MIC, Buzzer
	MIC = Sound_Sensor()
	Buzzer = Buzzer(port='A')

def main():
	base = 30
	while True:
		flag = []
		for i in range(base):
			tmp = MIC.read()
			print tmp
			flag.append(Threshold(tmp, threshold=200))
		if flag.count(1) >= 1:
			Buzzer.on()
		else:
			Buzzer.off()

def destroy():
	MIC.destroy()
	Buzzer.destroy()
	GPIO.cleanup()
	
if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		destroy()

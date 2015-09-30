#!/usr/bin/env python

from SunFounder_PiPlus import *

DT = DS1307()
while True:
	print DT.get_datetime()

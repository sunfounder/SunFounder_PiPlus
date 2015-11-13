#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import math
import random
import smbus
import time
import os
import commands
import threading

HOUR12 = 0		#12 hour clock defined
HOUR24 = 1		#24 hour clock defined

class DS1307(object):
	# DS1307 on Plus Shield
	def __init__(self, _clock = HOUR24):
		os.system('echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device')
		self._clockset = _clock
	
	def get_datetime(self):
		status, _datetime=commands.getstatusoutput('hwclock -r')
		return _datetime
		
	def get_date(self):
		_datetime = self.get_datetime()
		split_datetime = _datetime.split(' ')
		_date = [split_datetime[0], split_datetime[1], split_datetime[2], split_datetime[3]]
		_blank = ' '
		_date = _blank.join(_date)
		return _date
	
	def get_time(self):
		_time = self.get_datetime().split(' ')[4]
		if self._clockset == HOUR12 :
			_hour = int(_time.split(':')[0])
			if _hour > 11 :
				apm = 'PM'
			else:
				apm = 'AM'
			if _hour > 12 :
				_hour = _hour - 12
			if _hour == 0:
				_hour = 12
			if _hour < 10:
				_hour = '0%d' % _hour
			_time = '%s:%s:%s %s' % (_hour, _time.split(':')[1], _time.split(':')[2], apm)
		return _time
			
	def get_split_datetime(self):
		_datetime = self.get_datetime()
		split_datetime = _datetime.split(' ')
		_date = [split_datetime[0], split_datetime[1], split_datetime[2], split_datetime[3]]
		_time = split_datetime[4]
		if self._clockset == HOUR12 :
			_hour = int(_time.split(':')[0])
			if _hour > 11 :
				apm = 'PM'
			else:
				apm = 'AM'
			if _hour > 12 :
				_hour = _hour - 12
			if _hour == 0:
				_hour = 12
			if _hour < 10:
				_hour = '0%d' % _hour
			_time = '%s:%s:%s %s' % (_hour, _time.split(':')[1], _time.split(':')[2], apm)
		_blank = ' '
		_date = _blank.join(_date)
		return _date, _time


class PCF8591(object):
	# PCF8597 on Plus Shield
	_ADC_bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for Revision 1 boards
	def __init__(self, Address=0x48, _bus=_ADC_bus):
		super(PCF8591, self).__init__()
		self._address = Address
		self._bus = _bus

	def read(self, chn): #channel
		if chn == 0:
			self._bus.write_byte(self._address,0x40)
		if chn == 1:
			self._bus.write_byte(self._address,0x41)
		if chn == 2:
			self._bus.write_byte(self._address,0x42)
		if chn == 3:
			self._bus.write_byte(self._address,0x43)
		self._bus.read_byte(self._address) # dummy read to start conversion
		return self._bus.read_byte(self._address)
		
	def read_all(self):
		return self.read(0), self.read(1), self.read(2), self.read(3)
		
	def write(self, val):
		_temp = val # move string value to temp
		_temp = int(_temp) # change string to integer
		# print temp to see on terminal else comment out
		self._bus.write_byte_data(self._address, 0x40, _temp)
		
	def destroy(self):
		pass


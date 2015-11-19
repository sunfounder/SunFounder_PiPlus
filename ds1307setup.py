#!/usr/bin/env python
import os, time

def setup():
	monthname = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun',
				 '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
	monthfullname = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
					 '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
	os.system('echo ds1307 0x68 > /sys/class/i2c-adapter/i2c-1/new_device')
	check= ''
	while check != 'y' and check != 'Y' and check != 'n' and check != 'N':
		print '\nNow the DS1307 is:'
		time.sleep(0.5)
		os.system('hwclock -r')
		while True:
			check = raw_input('Is it right? Do you need to set the clock? (y/n)')
			if check == 'n' or check == 'N':
				print 'OK, we are done here. Installation finished.'
				quit()
			elif check == 'y' or check == 'Y':
				break
			else:
				print "\nSorry, I don't understand. I'm expecting a \"y\" or an \"n\" here. So try again. "

	print "\nLet's set the date!"
	confirm = None
	while confirm != True:
		flag = 1
		count_d = 0
		while flag == 1:
			while True:
				try:
					date = raw_input('\nType in year, month and date in this format: "YYYY/MM/DD": ')
					year = date.split('/')[0]
					month = date.split('/')[1]
					dateofmonth = date.split('/')[2]
					break
				except:
					print 'Error. Try again.'
			print ''
			if int(month) in [1, 3, 5, 7, 8, 10, 12]:
				if 0 < int(dateofmonth) < 32:
					flag = 0
				else:
					print '%s has only 31 days. Made a mistake? Try again.' % monthfullname[month]
			elif int(month) in [4, 6, 9, 11]:
				if 0 < int(dateofmonth) < 31:
					flag = 0
				else:
					print '%s has only 30 days. Made a mistake? Try again.' % monthfullname[month]
			elif int(month) == 2:
				if int(year)%4 == 0:
					if 0 < int(dateofmonth) < 30:
						flag = 0
					else:
						print '%s in %s has only 29 days. Fabruary has no more than 29 days even in a leap year! Made a mistake? Try again.' % (monthfullname[month], year)
				else:
					if 0 < int(dateofmonth) < 29:
						flag = 0
					elif int(dateofmonth) == 29: 
						print 'Year %s is a leap year, February has only 28 days. Made a mistake? Try again.' % year
					else:
						print "%s in %s has only 28 days. Even a leap year does not have that much days. Made a mistake? Try again." % (monthfullname[month], year)
			else:
				print 'How can it be month %s?! There are only 12 months a year %s. Maybe you made a mistake. Keep in mind: first year, then month, and finally date, each seprated by "/". Try again.' % (month, year)
			
			count_d += 1

		if count_d <= 1:
			print '\nGreat! Pretty easy huh?',

		elif count_d <= 2:
			print 'Well, we did it. ',
			
		elif count_d > 2:
			print 'Finally, we set the date. It took forever. But anyway.', 
			
		while True:
			print '\nYou set the date to: %s. %s, %s' % (monthname[month], dateofmonth, year)
			confirm = raw_input("Are you sure about that?(y/n) ")
			if confirm == 'y' or confirm == 'Y':
				confirm = True
				break
			elif confirm == 'n' or confirm == 'N':
				confirm = False
				break
			else:
				confirm = None
				print "Sorry, I don't understand. I'm expecting a \"y\" or an \"n\" here, so Try it again. "

	print "\nNow! Let's set the time!"
	confirm = None
	while confirm != True:
		flag = 1
		count_t = 0
		while flag == 1:
			while True:
				try:
					correnttime = raw_input('\nType in the corrent hour, minute and second in "HH:MM:SS" (in 24-hour time):')
					hour = correnttime.split(':')[0]
					minute = correnttime.split(':')[1]
					second = correnttime.split(':')[2]
					break
				except:
					print 'Error. Try again.'
			print ''
			if int(hour) <= 24:
				if int(hour) == 24:
					hour = 0
				flag = 0
			elif int(hour) > 24:
				print 'There are only 24 hours a day. Made a mistake? Try again.'

			elif int(minute) < 60:
				flag = 0
			elif int(minute) >= 60:
				print 'There are only 60 minutes an hour. Made a mistake? Try again.'

			elif int(second) < 60:
				flag = 0
			elif int(second) >= 60:
				print 'There are only 60 seconds a minute. Made a mistake? If you are sick of this second thing, just type 00, or any number less than 60. Try again.'

			count_t += 1

		if count_t <= 1 and count_d <= 1:
			print '\nBrilliant! Pretty easy huh?',

		if count_t <= 2:
			print 'Well, we did it. ',
			
		if count_t > 2:
			print 'Finally, we set the date. It took forever. But anyway.',

		while True:
			print '\nYou\'ve just set the corrent time to: %s:%s:%s' % (hour, minute, second)
			confirm = raw_input("Are you sure about that?(y/n) ")
			if confirm == 'y' or confirm == 'Y':
				confirm = True
				break
			elif confirm == 'n' or confirm == 'N':
				confirm = False
				break
			else:
				confirm = None
				print "Sorry, I don't understand. I'm expecting a \"y\" or an \"n\" here. Try again. "
				
	print "Great! Now I will correct the time for you."
	
	print 'Setting Linux time...'
	datetimesetting = month+dateofmonth+hour+minute+year+'.'+second
	os.system("date %s" % datetimesetting)
	print 'Done! Set Linux time to'
	os.system('date')
	
	print '\nSetting DS1307 from Linux time...'
	os.system('sudo hwclock -w')
	print 'Done! Set clock on DS1307 to:'
	os.system('sudo hwclock -r')

	print '\n\nOK, we are done here. Installation finished. Thank you for your support. \nIf anything goes wrong, copy or PrintScreen this log and send it to support@sunfounder.com'


if __name__ == "__main__":
	try:
		setup()
	except KeyboardInterrupt:
		pass
		

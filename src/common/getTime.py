# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-25

import time
import calendar

str_time = time.strftime("%Y-%m-%dT%H:%M:%SZ")


def get_daysTuple(year=None, mon=None):
	"""get the Year,Mon,Days of mon that current or you give"""
	if not (year and mon):
		year = time.localtime().tm_year
		mon = time.localtime().tm_mon
	month_days = calendar.monthrange(year, mon)
	return year, mon, month_days[-1]


def get_ymd():
	"""get Current time Year,Mon,Day"""
	s = time.localtime()
	year = s.tm_year
	mon = s.tm_mon
	day = s.tm_mday
	# week = s.wday
	return year, mon, day
	
	
if __name__ == '__main__':
	# print(get_daysTuple(2018, 2))
	# time_str = '-'.join(str(i).strip() for i in get_daysTuple())
	# time_tup = (str(i).strip() for i in get_daysTuple())
	# print(list(time_tup))
	# print(get_daysTuple())
	# print(dir(time.localtime()))
	print(get_ymd())
# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-12-12

import datetime
import time

t = time.time()  # 获取当前时间戳


def getTime(p=None):
	"""
	:param p:           需要输出的时间字符串格式
	:return:            当前时间戳根据指定格式返回对应字符串，默认返回年月日
	"""
	t_tup = time.localtime()  # 获取当前时间元组格式
	
	if p:
		t_str = time.strftime(p, t_tup)
	else:
		t_str = time.strftime("%Y-%m-%d", t_tup)
	return t_str


def timeToDate(_t):
	if len(str(_t)) >= 10:
		_t /= 1000
	l_t = time.localtime(_t)
	str_t = time.strftime("%Y-%m-%d", l_t)
	return str_t


def mondayOfWeek():
	"""
	:return:            获取本周周一日期
	"""
	dayOfWeek = datetime.datetime.now().isoweekday()
	nowDate = datetime.datetime.now()
	delta = datetime.timedelta(days=dayOfWeek - 1)
	monday = nowDate - delta
	return monday.strftime("%Y-%m-%d")


def monthDay():
	dayOfMonth = datetime.date.today().replace(day=1)
	return dayOfMonth.strftime("%Y-%m-%d")
	
if __name__ == '__main__':
	# print(timeToDate(1583390141000))
	print(monthDay())
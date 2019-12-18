# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-12-12

import datetime
import time

t = time.time()  # 获取当前时间戳


def getTime(p=None):
	
	t_tup = time.localtime()  # 获取当前时间元组格式
	
	if p:
		t_str = time.strftime(p, t_tup)
	else:
		t_str = time.strftime("%Y-%m-%d", t_tup)
	return t_str
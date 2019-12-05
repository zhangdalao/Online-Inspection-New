# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-11-20

"""基础类，用于读取INI配置文件"""

import os, sys
import configparser
from configparser import ConfigParser,RawConfigParser

sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
sys.path.append(root_path)


class GetDataIni:
	
	def __init__(self, filePath=None):
		if not filePath:
			filePath = f"{root_path}{sep}conf{sep}data.ini"
		
		# 简单配置文件使用该方法即可
		self.rfg = RawConfigParser()
		self.rfg.read(filePath, encoding="utf-8")
		
		# 当配置文件中数据存在变量, 且以 %(variable)s 的格式使用时用此种方法
		self.cfgB = ConfigParser(interpolation=configparser.BasicInterpolation())
		self.cfgB.read(filePath, encoding="utf-8")
	
		# 当配置文件中数据存在参数, 且以 ${variable} 的格式使用时用此种方法
		self.cfgE = ConfigParser(interpolation=configparser.ExtendedInterpolation())
		self.cfgE.read(filePath, encoding="utf-8")
		
	def normal_data(self, section, key):
		return self.rfg.get(section, key)
	
	def medium_data(self, section, key):
		return self.cfgB.get(section, key, raw=0)
	
	def high_data(self, section, key):
		return self.cfgE.get(section, key, raw=0)
	
if __name__ == '__main__':
	aa = GetDataIni()
	# print(aa.normal_data("Env", 'prod1'))
	# print(aa.cfgB.options("Env_name"))
	print(eval(aa.normal_data("Env_name", "1"))[0])
# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-25

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import time
import inspect


class HomeTest(TemplateTeseCase):
	"""首页模块"""
	
	# 通过文件名获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	
	@classmethod
	def setUpClass(cls):
		# 通过类名获取fieldname的值
		cls.dt = ReadJson(cls.project, cls.env)
		cls.dd_dt = cls.dt.get_robot_data()
		login_url = cls.dt.get_url("Login", "ByPassword")
		header = cls.dt.get_header()
		login_body = cls.dt.get_body()
		cls.s.post(url=login_url, headers=header, json=login_body)
		cls.fieldname = cls.__name__[:-4]

	def test_HomeInfo(self):
		"""HomeInfo接口"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			self.assertEqual(len(res["data"]), 6)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_ProfileInfo(self):
		"""ProfileInfo接口"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 30)
			self.assertEqual(res["data"]["staffId"], data["userId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_StaffMessage(self):
		"""StaffMessage接口"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]["storeMessage"]), 9)
			self.assertEqual(res["data"]["staffId"], data[1]["opId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_StaffOrg(self):
		"""StaffOrg接口"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			self.assertEqual(len(res), 4)
			self.assertEqual(type(res["data"]), list)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_SchedulePlanInfo(self):
		"""SchedulePlanInfo接口"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		data[0]["date"] = time.strftime("%Y-%m-%dT%H:%M:%SZ ")
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			self.assertEqual(len(res["data"]), 5)
			self.assertEqual(type(res["data"]["totalRecordNum"]), int)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
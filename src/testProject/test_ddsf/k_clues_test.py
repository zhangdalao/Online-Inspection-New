# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class CluesTest(TemplateTeseCase):
	"""网商卡线索模块"""
	
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
		
	def test_clueStaff(self):
		"""线索clueStaff"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 5)
			self.assertEqual(str(res["data"]["staffid"]), data[0]["staffId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_depDetail(self):
		"""线索depDetail"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 10)
			self.assertEqual(res["data"]["orgId"], data["orgId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_KPIByDepId(self):
		"""线索KPIByDepId"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["code"], 200)
			self.assertEqual(len(res), 4)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_StaffKPIDetail(self):
		"""线索StaffKPIDetail"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["code"], 200)
			self.assertEqual(len(res), 4)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listAchievement(self):
		"""线索StaffKPIDetail"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["code"], 200)
			self.assertEqual(len(res), 4)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
		
# TODO 需要修改请求参数的时间修改为动态参数
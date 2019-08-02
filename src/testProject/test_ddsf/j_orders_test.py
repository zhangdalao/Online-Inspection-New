# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class OrdersTest(TemplateTeseCase):
	"""网商卡订单模块"""
	
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
		
	def test_orders(self):
		"""默认全部网商卡订单"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 4)
			if res["data"]["total"] > res["data"]["pageSize"]:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["total"])
			print(res["data"]["total"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_orders_case1(self):
		"""网商卡订单_待收款"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data["haveContract"] = False
		data["orderStatuses"] = [0]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 4)
			if res["data"]["total"] > res["data"]["pageSize"]:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["total"])
			print(res["data"]["total"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_orders_case2(self):
		"""网商卡订单_待审核"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data["haveContract"] = True
		data["orderStatuses"] = [0]
		data["auditStatus"] = 0
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 4)
			if res["data"]["total"] > res["data"]["pageSize"]:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["total"])
			print(res["data"]["total"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_orders_case3(self):
		"""网商卡订单_待收款"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data["orderStatuses"] = [1]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 4)
			if res["data"]["total"] > res["data"]["pageSize"]:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["orders"]), res["data"]["total"])
			print(res["data"]["total"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
# TODO 需要补充完整订单数据，不然订单详情以及运行日志接口无法调用
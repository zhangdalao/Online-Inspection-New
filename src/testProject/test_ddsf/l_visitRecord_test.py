# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class VisitRecordTest(TemplateTeseCase):
	"""拜访门店模块"""
	
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
	
	def test_RecordPage(self):
		"""拜访记录--默认列表"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case1(self):
		"""拜访记录-组织架构-测试部门"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["depIds"] = [189]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case2(self):
		"""拜访记录-组织架构-某个普通商服"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0].pop("isManager")  # 去除商服主管角色
		data[0].pop("depIds")  # 去掉部门参数
		data[0]["serviceIds"] = [2884837]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case3(self):
		"""拜访记录--区域板块--白山"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["cityIds"] = [10204]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case4(self):
		"""拜访记录--拜访目的--客情维护"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["purposeList"] = [1]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case5(self):
		"""拜访记录--时间筛选--七月"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["startDate"] = 1561910400000
		data[0]["endDate"] = 1564588799999
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case6(self):
		"""规划拜访--默认列表"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case7(self):
		"""规划拜访-组织架构-测试部门"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		data[0]["depIds"] = [189]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case8(self):
		"""规划拜访-组织架构-某个普通商服"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		data[0].pop("isManager")  # 去除商服主管角色
		data[0].pop("depIds")  # 去掉部门参数
		data[0]["serviceIds"] = [2884837]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case9(self):
		"""规划拜访--区域板块--白山"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		data[0]["cityIds"] = [10204]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case10(self):
		"""规划拜访--拜访目的--客情维护"""
		self.apiName = (inspect.stack()[0][3])[5:-7]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		data[0]["purposeList"] = [1]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_RecordPage_case11(self):
		"""规划拜访--时间筛选--七月"""
		self.apiName = (inspect.stack()[0][3])[5:-7]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["step"] = 1
		data[0]["startDate"] = 1561910400000
		data[0]["endDate"] = 1564588799999
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			elif res["data"]["totalRecord"] == 0:
				self.assertEqual(res["data"]["results"], None)
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))

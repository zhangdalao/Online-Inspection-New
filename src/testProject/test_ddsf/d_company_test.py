# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class CompanyTest(TemplateTeseCase):
	"""公司资源"""
	
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
	
	def test_CompanyList(self):
		"""公司列表"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case1(self):
		"""公司列表>网商卡"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["hasNetCard"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case2(self):
		"""公司列表>平台通"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["isPlatform"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case3(self):
		"""公司列表>经纪通"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["isEconomic"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case4(self):
		"""公司列表>KA"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["isKa"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case5(self):
		"""公司列表>多多云销"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["isSaas"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
	
	def test_CompanyList_case6(self):
		"""公司列表>云验真"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里把网商卡条件参数加上去
		data[0]["isCloudCheck"] = True
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= 20:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
			
# TODO 这里用例均是默认为确认返回结果的，所以还需要补充参数为："isNeedResults" 为False的情况

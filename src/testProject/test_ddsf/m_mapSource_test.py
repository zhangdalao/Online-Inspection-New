# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class MapSourceTest(TemplateTeseCase):
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
	
	def test_CityDistrict(self):
		"""城市区域列表-白山"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			print(data)
			res = result.json()
			self.assertEqual(len(res["data"]), 10)
			self.assertIn("districtName", res["data"][0])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_CityDistrict_case1(self):
		"""城市区域列表-切换城市-深圳"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["cityId"] = 1337
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 13)
			self.assertIn("districtName", res["data"][0])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_CitySection(self):
		"""城市区域板块列表-深圳"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["cityId"] = 1337
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 87)
			self.assertIn("sectionName", res["data"][0])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_StoreInfoList(self):
		"""地图门店区域列表"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertGreaterEqual(len(res["data"]), 3)
			self.assertEqual(res["data"][0]["cityId"], data[0]["cityId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_StoreByCodition(self):
		"""门店列表-地图区域条件"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertGreaterEqual(len(res["data"]["results"]), 3)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
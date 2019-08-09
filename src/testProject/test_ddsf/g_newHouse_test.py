# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26


import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class NewHouseTest(TemplateTeseCase):
	"""新房通模块"""
	
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
	
	def test_listCity(self):
		"""城市列表"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			# 319个城市
			self.assertEqual(len(res["data"]), 319)
			self.assertEqual(res["data"][0]["regionId"], 121)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listHouse(self):
		"""我的主推楼盘列表"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listHouse_case1(self):
		"""我的主推楼盘列表_根据城市区域筛选>宜昌"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["cityIds"] = [9528]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listHouse_case2(self):
		"""选中某个城市（上海）>所有楼盘"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0].pop("merchantService")
		data[0]["cityIds"] = [121]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listHouse_case3(self):
		"""商服权限城市>城市区域>白山>浑江楼盘列表"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0].pop("merchantService")
		data[0]["cityIds"] = [10204]
		data[0]["districtIds"] = [10205]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			if res["data"]["totalRecord"] >= data[0]["pageSize"]:
				self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
			else:
				self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
			print(res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	# TODO 这里业务特色存在确认按钮，接口层面却没做区分，需要跟开发反馈
	# TODO 后期补充业务特色接口用例
	
	def test_XfdkStoreData(self):
		"""楼盘与商户之间的报备带看数据"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_HouseDetail(self):
		"""楼盘具体详情"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res), 4)
			self.assertIn(["独家"], res["data"]["panInfoDto"]["tagList"])  # 这里tagList的值会发生变化
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_ConfigList(self):
		"""楼盘配置信息"""
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
			raise Exception(str(er))
		
	def test_ShareTemplate(self):
		"""根据楼盘信息获取楼盘海报模板"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		headers = copy.deepcopy(self.dt.get_header())
		# 这个get接口很特殊，需要增加一些特殊字段
		headers_para = {"opId": "6520137", "opName": "%E9%99%88%E6%96%87%E5%BB%BA", "Restful": '{"house_id": "52242"}',
		                "systemsource": "DD_COMMERCIAL"}
		headers.update(headers_para)
		try:
			result = self.s.get(url=url, headers=headers)
			res = result.json()
			self.assertGreaterEqual(len(res["data"]["templates"]), 2)
			# print(res["data"]["estateId"], eval(headers_para["Restful"])["house_id"])
			self.assertEqual(str(res["data"]["estateId"]), eval(headers_para["Restful"])["house_id"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
# TODO 需要补充自定义海报相关接口
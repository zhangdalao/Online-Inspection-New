# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26


import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class AgentTest(TemplateTeseCase):
	"""经纪人模块"""
	
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
		
	def test_listAgent(self):
		"""公司列表默认筛选条件"""
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
		
	def test_listAgent_case1(self):
		"""公司列表>商户服务>我服务的"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["staffIds"] = [6520137]
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
		
	def test_listAgent_case2(self):
		"""公司列表>实名情况>不限=已认证+未实名"""
		para_name = "verifiedStatus"
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		res = []
		try:
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = "result" + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(len(locals()[name]["data"]["results"]), locals()[name]["data"]["totalRecord"])
				print(locals()[name]["data"]["totalRecord"])
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_listAgent_case3(self):
		"""公司列表>名片情况>不限=已认证+未上传"""
		para_name = "userCardStatus"
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		res = []
		try:
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = "result" + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(len(locals()[name]["data"]["results"]), locals()[name]["data"]["totalRecord"])
				print(locals()[name]["data"]["totalRecord"])
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
			
	def test_listAgent_case4(self):
		"""公司列表>名片情况>不限=已认证+未上传"""
		para_name = "storeStatus"
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		res = []
		try:
			for i in range(3):
				data[0][para_name] = i
				print(data)
				name = "result" + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(len(locals()[name]["data"]["results"]), locals()[name]["data"]["totalRecord"])
				print(locals()[name]["data"]["totalRecord"])
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
			
# TODO 这里目前只做了单一筛选条件处理，多筛选条件组合情况过多，还没处理，后期完善
# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common import getTime
from src.common.dingding import send_ding
import inspect
import copy


class DatasTest(TemplateTeseCase):
	"""数据中心模块"""
	
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
		
	def test_XfdkAchievementData(self):
		"""新房导客数据"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertIn("monthPurchaseCount", res["data"])
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_XfdkStoreData(self):
		"""新房导客门店数据"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里需要根据脚本执行时间去获取当前时间模拟情景
		time_list = list(str(i).strip() for i in getTime.get_daysTuple())
		data["startDate"] = "%s-%s-01" % (time_list[0], time_list[1])
		data["endDate"] = '-'.join(time_list)
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertIn("reportAgentNum", res["data"])
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_XfdkStoreData_case1(self):
		"""新房导客门店数据>门店位置筛选"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里需要根据脚本执行时间去获取当前时间模拟情景
		time_list = list(str(i).strip() for i in getTime.get_daysTuple())
		data["startDate"] = "%s-%s-01" % (time_list[0], time_list[1])
		data["endDate"] = '-'.join(time_list)
		data["cityIds"] = [10204]
		data["districtIds"] = [10205]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertIn("reportAgentNum", res["data"])
			self.assertIn("bespokenNum", res["data"])
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			
	def test_XfdkStoreData_case2(self):
		"""新房导客门店数据>所属项目筛选"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里需要根据脚本执行时间去获取当前时间模拟情景
		time_list = list(str(i).strip() for i in getTime.get_daysTuple())
		data["startDate"] = "%s-%s-01" % (time_list[0], time_list[1])
		data["endDate"] = '-'.join(time_list)
		data["houseIdList"] = [2029540]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertIn("reportAgentNum", res["data"])
			self.assertIn("bespokenNum", res["data"])
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_XfdkStoreData_case3(self):
		"""新房导客门店数据>更改时间>历史业绩+项目筛选"""
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 这里指定指定7月份该商服某个项目，因为已经是过去数据不会被修改；
		data["houseIdList"] = [2029540]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["data"]["reportAgentNum"], 6)
			self.assertEqual(res["data"]["subscribeAgentNum"], 2)
			self.assertEqual(res["data"]["bespokenNum"], 1)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_searchLoupan(self):
		"""项目楼盘搜索"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			if res["data"]:
				self.assertIn(data["keyWord"], res["data"][0]["projectName"])
			else:
				self.assertEqual(type(res["data"], list))
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			
	def test_AchievementStat(self):
		"""新房分销数据旧版>AchievementStat"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["code"], 200)
			self.assertEqual(len(res["data"]), 13)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			
	def test_ActiveAgentNum(self):
		"""新房分销数据旧版>ActiveAgentNum"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 2)
			self.assertIn("newActiveAgentNum", res["data"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_NewHouseGuideData(self):
		"""新房分销数据旧版>NewHouseGuideData"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 8)
			self.assertIn("monthReportAgentNum", res["data"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_AchievementList(self):
		"""新房分销数据旧版>AchievementList"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		try:
			for i in range(1, 5):
				data["actionType"] = str(i)
				name = "result" + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				self.assertEqual(len(locals()[name]["pageInfo"]), 4)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

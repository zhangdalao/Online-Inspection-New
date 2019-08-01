# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-26

import os
from src.common.template import TemplateTeseCase
from src.common.read_json import ReadJson
from src.common.dingding import send_ding
import inspect
import copy


class StoreTest(TemplateTeseCase):
	"""门店资源列表"""
	
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
		
	def test_StoreList(self):
		"""(确认)获取我负责门店资源"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		# print(data)
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(res["success"], True)
			self.assertEqual(len(res["data"]), 6)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_StoreList_case1(self):
		"""(未确认)公海门店资源>服务商服>不限=无人+他人"""
		para_name = "staffStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body("StoreList_paras")
		# print(data)
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			# print(res)
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"]+res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_StoreList_case2(self):
		"""(未确认)负责门店资源>上门拜访>不限=30天内+30天外"""
		para_name = "visitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 添加参数isNeedResults
		data[0]["isNeedResults"] = False
		# print(data)
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"]+res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case3(self):
		"""(未确认)负责门店资源>电话拜访>不限=30天内+30天外"""
		para_name = "telVisitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		# 添加参数isNeedResults
		data[0]["isNeedResults"] = False
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"]+res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case4(self):
		"""(未确认)公海门店资源>上门拜访>不限=30天内+30天外"""
		para_name = "visitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body("StoreList_paras"))
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"]+res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case5(self):
		"""(未确认)公海门店资源>电话拜访>不限=30天内+30天外"""
		para_name = "telVisitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body("StoreList_paras")
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"]+res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case6(self):
		"""(未确认)公海门店资源>服务商服>不限=无人+他人"""
		para_name = "staffStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body("StoreList_paras")
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				res.append(locals()[name])
			# print(res)
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_StoreList_case7(self):
		"""(确认)负责门店资源>上门拜访>不限=30天内+30天外"""
		para_name = "visitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		# print(data)
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(locals()[name]["data"]["totalRecord"], len(locals()[name]["data"]["results"]))
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_StoreList_case8(self):
		"""(确认)负责门店资源>电话拜访>不限=30天内+30天外"""
		para_name = "telVisitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(locals()[name]["data"]["totalRecord"], len(locals()[name]["data"]["results"]))
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case9(self):
		"""(确认)公海门店资源>上门拜访>不限=30天内+30天外"""
		para_name = "visitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-6]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(locals()[name]["data"]["totalRecord"], len(locals()[name]["data"]["results"]))
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))

	def test_StoreList_case10(self):
		"""(确认)公海门店资源>电话拜访>不限=30天内+30天外"""
		para_name = "telVisitStatus"
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:-7]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			res = []
			for i in range(3):
				data[0][para_name] = i
				# print(data)
				name = 'result' + str(i)
				locals()[name] = self.s.post(url=url, json=data).json()
				if locals()[name]["data"]["totalRecord"] >= data[0]["pageSize"]:
					self.assertEqual(len(locals()[name]["data"]["results"]), data[0]["pageSize"])
				else:
					self.assertEqual(locals()[name]["data"]["totalRecord"], len(locals()[name]["data"]["results"]))
				# print(locals()[name]["data"]["totalRecord"])
				res.append(locals()[name])
			self.assertEqual(res[0]["data"]["totalRecord"], res[1]["data"]["totalRecord"] + res[2]["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_StoreList_case11(self):
		"""(确认)负责门店资源>区域板块>白山-浑江"""
		self.apiName = (inspect.stack()[0][3])[5:-7]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = copy.deepcopy(self.dt.get_body())
		data[0]["cityIds"] = [10204]
		data[0]["districtIds"] = [10205]
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_OrgStore(self):
		"""商服主管门店资源组织架构数据"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]), 6)
			self.assertGreaterEqual(res["data"]["allStoreCount"], 293)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_listAllStaff(self):
		"""商服所在城市公司所有商服人员"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertGreater(len(res["data"]), 79)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	def test_OrgTree(self):
		"""商服所在城市公司组织架构"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertGreaterEqual(len(res["data"]["subDepInfoList"]), 6)
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
	
	def test_RegionByCityId(self):
		"""选定城市区域"""
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		data = self.dt.get_body()
		try:
			result = self.s.post(url=url, json=data)
			res = result.json()
			self.assertEqual(len(res["data"]["childs"]), 8)
			self.assertEqual(res["data"]["data"]["regionId"], data["cityId"])
		except Exception as er:
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
		
	# TODO 添加门店线索-筛选条件合作情况的用例，组合情况有点多，这里需求也存在缺陷，顾后面是确认后再实现

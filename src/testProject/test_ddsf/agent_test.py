# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-10-28


import inspect
import ddt
from src.common.runTest import *
from src.common.dingDing import send_ding
from src.common.read_data import ReadData
import os, sys
count = 0


@ddt.ddt
class AgentTest(RunTest):
	"""地图找店模块"""
	
	# 通过文件名夹获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	# 读取文件实例化
	a = ReadData(project, project)
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
	# 获取项目名后，获取机器人相关配置
	json_dict = a.json_data[project]["robot_data"]
	robot_url = json_dict["robot_url"]
	mobile = json_dict["mobile"]
	
	@classmethod
	def setUpClass(cls):
		cls.env_num = cls.a.get_num_name("环境")
		cls.apiName_num = cls.a.get_num_name("接口名称")
		cls.method_num = cls.a.get_num_name("请求方法")
		cls.headers_num = cls.a.get_num_name("请求头")
		cls.para_num = cls.a.get_num_name("请求参数")
		cls.desc_num = cls.a.get_num_name("用例描述")
		cls.data_num = cls.a.get_num_name("请求体")
		cls.expect_num = cls.a.get_num_name("预期结果")
		cls.isSkip_num = cls.a.get_num_name("是否跳过该用例")
		cls.relateData_num = cls.a.get_num_name("接口关联参数")
	
	def setUp(self):
		globals()['count'] += 1
		self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))
	
	def tearDown(self):
		if self.result and type(self.result) != str:
			try:
				self.assertEqual(True, checkOut(self.res, self.expect))
				self.logger.debug("测试结果         :测试通过！")
			except Exception as err:
				self.logger.error("测试结果         :测试失败！")
				send_ding(self.robot_url, self.mobile,
				          content=f"{self.desc}测试失败！\n接口返回为：{self.res}, 预期结果为：{self.expect}")
				raise err
		elif self.result and type(self.result) == str:
			send_ding(self.robot_url, self.mobile, content=f"{self.desc}测试失败！\n测试反馈:{self.result}")
			raise Exception
		self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))
	
	@ddt.data(*a.get_data_by_api(fieldname, "listAgent"))
	def test_listAgent(self, value):
		"""经纪人列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss["cityIds_agent"] = ["3", "450", "619", "852", "1406", "2179", "9393", "10204"]
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "getAgentDetailInfo"))
	def test_getAgentDetailInfo(self, value):
		"""经纪人详情信息"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss["agentId"] = 6537143
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "getCityMap"))
	def test_getCityMap(self, value):
		"""城市列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "getClueList"))
	def test_getClueList(self, value):
		"""指定经纪人线索列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss["agentId_str"] = str(sss["agentId"])
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value, cookies=sss["cookies"])
		
	@ddt.data(*a.get_data_by_api(fieldname, "getCompany"))
	def test_getCompany(self, value):
		"""获取指定公司信息"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss["companyId"] = 82200912
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value, cookies=sss["cookies"])
		
	@ddt.data(*a.get_data_by_api(fieldname, "getOrgNetCardData"))
	def test_getOrgNetCardData(self, value):
		"""根据ID获取经纪人网商卡数据"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "listStoreOrCompanyAgent"))
	def test_listStoreOrCompanyAgent(self, value):
		"""根据经纪人获得门店店长信息"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss["storeId"] = 82351552
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
		                         value)
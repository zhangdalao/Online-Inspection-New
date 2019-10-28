# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-18


import inspect
import ddt
from src.common.runTest import *
from src.common.dingDing import send_ding


count = 0


@ddt.ddt
class AgentDynamicTest(RunTest):
	"""经纪动态模块"""
	
	# 通过文件名夹获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	# 读取文件实例化
	a = ReadData(project, project)
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
	
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
		if self.result:
			try:
				self.assertEqual(True, checkOut(self.res, self.expect))
				self.logger.debug("测试结果         :测试通过！")
			except Exception as err:
				self.logger.error("测试结果         :测试失败！")
				json_dict = self.a.json_data[self.project]["robot_data"]
				robot_url = json_dict["robot_url"]
				mobile = json_dict["mobile"]
				send_ding(robot_url, mobile, content=f"{self.desc}测试失败！接口返回为：{self.res}, 接口预期结果为：{self.expect}")
				raise err
		self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))
	
	@ddt.data(*a.get_data_by_api(fieldname, "AgentDynamic"))
	def test_AgentDynamic(self, value):
		"""经纪动态列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
	
	@ddt.data(*a.get_data_by_api(fieldname, "DynamicDetail"))
	def test_DynamicDetail(self, value):
		"""经纪动态-详情"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreList"))
	def test_StoreList(self, value):
		"""经纪动态-最近拜访门店列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		sss['cityIds'] = ["121", "852", "1406", "10204"]
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreByStoreId"))
	def test_StoreByStoreId(self, value):
		"""经纪动态-门店详情"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreMessage"))
	def test_StoreMessage(self, value):
		"""经纪动态-门店拜访选项字段"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
		
	@ddt.data(*a.get_data_by_api(fieldname, "VisitDynamic"))
	def test_VisitDynamic(self, value):
		"""经纪动态-门店拜访选项字段"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		data_dict = {"estateId": 51443, "storeId": 82200915, "dynamicTags": 12, "reVisitType": 3}
		sss.update(data_dict)
		self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
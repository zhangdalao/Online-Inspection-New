# -*- coding=utf-8 -*-
# Author: Zhou Cuiling
# @Date : 2019-09-21


import inspect
import ddt,sys
from src.common.read_data import ReadData
from src.common.runTest import *
from src.common.dingDing import send_ding
from src.testProject.test_sybb import read_cookie
import json

count = 0


@ddt.ddt
class FactoringTest(RunTest):
	"""业务订单风控模块"""
	
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
		cls.cookies = json.loads(read_cookie.readcookie().replace("\'", '\"'))

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

	@ddt.data(*a.get_data_by_api(fieldname, "Changechannel"))
	def test_Changechannel(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
							self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "1_OrderList"))
	def test_1_OrderList(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
							self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=self.cookies)


	@ddt.data(*a.get_data_by_api(fieldname, "Ordersummary"))
	def test_Ordersummary(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "OrderManage"))
	def test_OrderManage(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "OrderchannelId"))
	def test_OrderchannelId(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "Orderid"))
	def test_Orderid(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "OrderprogramId"))
	def test_OrderprogramId(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "2_OrderInfo"))
	def test_2_OrderInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "HouseInfo"))
	def test_HouseInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "AgentInfo"))
	def test_AgentInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "AttachmentInfo"))
	def test_AttachmentInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "OrderLogs"))
	def test_OrderLogs(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "ProjectInfo"))
	def test_ProjectInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

	@ddt.data(*a.get_data_by_api(fieldname, "3_ProjectRepayPlan"))
	def test_3_ProjectRepayPlan(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)


	@ddt.data(*a.get_data_by_api(fieldname, "ProjectApplyInfo"))
	def test_ProjectApplyInfo(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
								 self.para_num,
								 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
								 cookies=self.cookies)

if __name__ == '__main__':
	unittest.main()
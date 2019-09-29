# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
import requests
from src.common.dingDing import send_ding
from src.testProject.test_saas_rent.base_login import rent_saas_login

count = 0


@ddt.ddt
class Rent_InspectTest(RunTest):
	"""实勘模块"""
	
	# 通过文件名夹获取project参数的值
	project = os.path.dirname(__file__)[-9:]
	print(project)
	# 读取文件实例化
	a = ReadData(project,'saas_rent')
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
	print(fieldname)

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
		cls.cookie_txt = rent_saas_login()
		print("房号为：",sss["roomNo"])

	
	def setUp(self):
		globals()['count'] += 1
		self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))
	
	def tearDown(self):
		self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

	@ddt.data(*a.get_data_by_api(fieldname, "add_Rent_Inspect"))  #接口对应的名称
	def test_01_add_Rent_Inspect(self, value):
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[8:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		# 调用接口发起请求
		res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
		                    self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,cookies=self.cookie_txt)
		try:
			self.assertEqual(True, checkOut(self.res, self.expect))
			self.logger.info("测试结果         :测试通过！")
		except Exception as err:
			self.logger.error("测试结果         :测试失败！")
			# json_dict = self.a.json_data[self.project]["robot_data"]
			# robot_url = json_dict["robot_url"]
			# mobile = json_dict["mobile"]
			# send_ding(robot_url, mobile, content=f"添加实勘异常！接口返回为：{res}, 接口预期结果为：{self.expect}")
			raise err

if __name__ == '__main__':
	unittest.main()
# -*- coding=utf-8 -*-
# Author: Zhou Cuiling
# @Date : 2019-09-21


import inspect
import ddt,sys
from src.common.read_data import ReadData
from src.common.runTest import *
from src.common.dingDing import send_ding
from src.common.sms_code import get_smsCode
import requests

count = 0


@ddt.ddt
class LoginTest(RunTest):
	"""登录模块"""
	
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
		t = time.time()
		cls.timestamp = str(round(t * 1000))
		sss["timestamp"] = cls.timestamp
		
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

	@ddt.data(*a.get_data_by_api(fieldname, "Login"))
	def test_Login(self, value):
		if sss["env"] == "prod":
			sss["sms_code"] = get_smsCode("prod", 'https://jr.fangdd.com/jgj/api/user/smgsend', 'post', json={"mobile":"13058019302","type":1})
		elif sss["env"] == "pre":
			sss["sms_code"] = get_smsCode("pre", 'https://jr.fangdd.com.cn/jgj/api/user/smgsend', 'post', json={"mobile":"13682521706","type":1})
		elif sss["env"] == "test":
			sss["sms_code"] = get_smsCode("test", 'https://jr.fangdd.net/jgj/api/user/smgsend', 'post', json={"mobile":"13682521706","type":1})
		# 通过函数名获取apiName参数的值
		print("sss等于",sss)
		self.apiName = (inspect.stack()[0][3])[5:]
		# 获取测试环境参数
		env = value[self.env_num]
		# 通过环境参数获得接口url
		uri = self.a.get_apiPath(self.fieldname, self.apiName)
		url = self.a.get_domains()[env] + uri
		# 调用接口发起请求
		self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
		                         self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
		# print(type(result.cookies))
		if self.res and self.res["code"] == '200':
			# sss["jgj_cookies"] = result.cookies
			par_dir = os.path.dirname(__file__)
			sep = os.sep
			data_file = open(f'{par_dir}{sep}jgj_cookie.txt', "w",encoding="utf-8")
			data_file.write(str(requests.utils.dict_from_cookiejar(self.result.cookies)))
			data_file.close()


if __name__ == '__main__':
	unittest.main()
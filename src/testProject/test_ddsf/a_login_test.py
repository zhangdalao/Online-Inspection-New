# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-23


import unittest
from src.common.read_json import ReadJson
from src.common.template import TemplateTeseCase
from src.common.dingding import send_ding
from src.common import log
import os
import inspect
import requests


class LoginTest(TemplateTeseCase):
	"""登录模块"""
	
	# 通过文件名获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	# env = "prod"
	
	@classmethod
	def setUpClass(cls):
		# 通过类名获取fieldname的值
		cls.fieldname = cls.__name__[:-4]
		cls.dt = ReadJson(cls.project, cls.env)
		# 分项目组获取对应钉钉推送参数
		cls.dd_dt = cls.dt.get_robot_data()
		
	def test_ByPassword(self):
		"""用户名密码登录"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		url = self.dt.get_url(self.fieldname, self.apiName)
		# headers = self.dt.get_header()
		data = self.dt.get_body()
		try:
			# 调用账号密码登录接口
			# result = requests.post(url=url, headers=headers, json=data)
			result = requests.post(url=url, json=data)
			# print(result.elapsed)
			res = result.json()
			# 进行断言
			self.assertEqual(res["code"], 200)
			self.assertEqual(res["data"]["userId"], 6520137)
		except Exception as er:
			log.logger_error.error("%s模块下%s接口异常:" % (self.fieldname, self.apiName) + str(er))
			send_ding(self.dd_dt["robot_url"], self.dd_dt["mobile"], "%s模块下%s接口异常:" % (self.fieldname, self.apiName) +
			          str(er))
			raise Exception(str(er))
		
	def test_ByVerifyCode(self):
		"""用户名密码登录"""
		pass

# TODO 补充验证码登录的用例

if __name__ == '__main__':
	unittest.main()


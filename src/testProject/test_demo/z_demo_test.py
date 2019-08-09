# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-07

import unittest
import requests
import HTMLTestReportCN
import os
import json


class DemoTest(unittest.TestCase):
	
	s = requests.session()

	def test_queryCityList_test(self):
		self.s.post(url="https://as-web.fangdd.net/ioux/loginByPassword/",
		                        json={"username": "linyuanwei@fangdd.com", "password": "ASDFasdf1"}, )
		res = self.s.post(url="https://as-web.fangdd.net/ioux/queryCityList", json={})
		# print(res.json())
		try:
			if res.json()["data"] and res.status_code == 200:
				res_time = res.elapsed.microseconds / 1000
				print("此次接口响应时间为：%dms" % res_time)
		except Exception as er:
			raise Exception(str(er))
		
	# def test_queryCityList_prod(self):
	# 	self.s.post(url="https://as-web.fangdd.com/ioux/loginByPassword/",
	# 	                        json={"username": "linyuanwei@fangdd.com", "password": "ASDFasdf1"}, )
	# 	res = self.s.post(url="https://as-web.fangdd.com/ioux/queryCityList", json={})
	# 	# print(res.json())
	# 	try:
	# 		if res.json()["data"] or res.status_code == 200:
	# 			res_time = res.elapsed.microseconds / 1000
	# 			print("此次接口响应时间为：%d" % res_time)
	# 	except Exception as er:
	# 		raise Exception(str(er))
		
tmp = os.sep
if __name__ == '__main__':
	suite = unittest.TestSuite()
	cases = unittest.defaultTestLoader.loadTestsFromTestCase(DemoTest)
	for i in range(100):
		suite.addTests(cases)
	# suite.addTests(cases)
	HTMLTestReportCN.HTMLTestRunner(stream=open(os.path.abspath(os.path.join(os.getcwd(), "../../..")) + tmp +
		                                            'output/report' + tmp + 'report.html', 'wb'),
		                                title='多多商服接口自动化测试报告', tester='Bo_lin Chen').run(suite)

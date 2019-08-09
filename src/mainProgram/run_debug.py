# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-24


import unittest
import HTMLTestReportCN
import os

from src.common.template import TemplateTeseCase
# from src.testProject.test__ddsf import a_login_test, b_home_test
from src.testProject.test_ddsf import c_store_test
from src.testProject import test_ddsf

tmp = os.sep

if __name__ == '__main__':
	# # 方式1：控制单条用例执行
	# suite = unittest.TestSuite()
	# # suite.addTest(a_login_test.LoginTest('test_ByPassword'))
	# # suite.addTest(b_home_test.HomeTest('test_HomeInfo'))
	# suite.addTest(c_store_test.StoreTest('test_getOrgStore'))
	# HTMLTestReportCN.HTMLTestRunner(stream=open(os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	#                                             'output/report' + tmp + 'report.html', 'wb'),
	#                                 title='多多商服接口自动化测试报告', description=TemplateTeseCase.env + "环境测试报告",
	#                                 tester='Bo_lin Chen').run(suite)
	
	# 方式2：通过case文件名指定接口测试

	suite = unittest.defaultTestLoader.discover(start_dir=os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	                                                      'src/testProject/test_ddsf', pattern='m_mapSource_test.py')
	# # suite.addTests(suite2)
	# suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='*.py')
	HTMLTestReportCN.HTMLTestRunner(stream=open(os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	                                            'output/report' + tmp + 'report.html', 'wb'),
	                                title='多多商服接口自动化测试报告', description=TemplateTeseCase.env + "环境测试报告",
	                                tester='Bo_lin Chen').run(suite)

	# 方式3：通过正则指定所有接口
	# suite = unittest.defaultTestLoader.discover(start_dir=os.getcwd() + tmp + 'Cases', pattern='*.py')
	# HTMLTestReportCN.HTMLTestRunner(stream=open(os.getcwd() + tmp + 'Output' + tmp + 'report.html', 'wb'),
	#                                 title='多多商服接口自动化测试报告', description=TemplateTeseCase.env + "环境测试报告",
	#                                 tester='Bo_lin Chen').run(suite)

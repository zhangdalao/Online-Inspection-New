# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import os, sys
import json

sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
sys.path.append(root_path)



import unittest
from src.common.BeautifulReport import BeautifulReport
# from BeautifulReport import BeautifulReport
from src.common.dingDing import send_link
from time import sleep
import socket
import time


# # 获取本机计算机名称
# hostname = socket.gethostname()
# # 获取本机ip
# ip = socket.gethostbyname(hostname)


def get_project_robot_URL(projectName=None):
	json_path = f"{root_path}{sep}data{sep}jsonFiles{sep}{projectName}.json"
	# 读取json数据文件中的内容
	with open(json_path, "r", encoding="utf-8") as j:
		json_data = json.load(j)
	return json_data


def start(cases_dir=None):
	# 脚本运行时间
	now = time.strftime("%Y_%m_%d-%H_%M_%S")
	now_day = time.strftime("%Y_%m_%d")

	# 判断是否有指定用例文件夹
	if cases_dir:
		project_dir = cases_dir  # test_xxxx
		project_name = project_dir.split("test_")[-1]  # xxxx
		robot_url = get_project_robot_URL(project_name)[project_name]["robot_data"]["robot_url"]
		suites_dir = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + sep.join(['src', 'testProject',
		                                                                                          f'{project_dir}'])
		suite = unittest.defaultTestLoader.discover(start_dir=suites_dir, pattern='*1_test.py')
		reportFileName = project_name + f'_{now}_result.html'
		
	else:
		# 这里需要补充测试组机器人URL
		robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=d852c17cf61d26bfbaf8d0d8d4927632f9b1712cb9aa145342159f8fd0065fc4'
		suites_dir = root_path + f'{sep}src{sep}testProject'
		suite = unittest.defaultTestLoader.discover(start_dir=suites_dir, pattern='*_test.py')
		reportFileName = 'All' + f'_{now}_result.html'

	reportDirName = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + 'output' + sep + 'report' + sep
	
	report_dir = 'report_{_now}'.format(_now=now_day)
	reportDir = reportDirName + report_dir
	
	while not os.path.exists(reportDir):
		try:
			os.makedirs(reportDir)
			break
		except OSError as e:
			if e.errno != os.errno.EEXIST:
				raise
			# time.sleep might help here
			pass
	
	with open(reportDir + sep + reportFileName, "wb"):
		beaRep = BeautifulReport(suite)
		res = beaRep.report(filename=reportFileName, description='接口自动化测试', report_dir=reportDir)
	# return res
	sleep(5)
	ip = '10.0.6.56'
	result_url = "http://" + ip + f':8686{sep}{report_dir}{sep}{reportFileName}'
	# print(f'{sep}{reportFileName}')  # /2019_09_11-19_42_30_result.html
	# print(result_url)
	if robot_url:
		send_link(robot_url, result_url, '房多多接口自动化测试报告')
	return res

if __name__ == '__main__':
	# start("https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf2b498bcece2644a")
	# get_project_robot_URL()
	# start('test_saas_rent')
	# print(os.getcwd())
	start("test_ddsf")
	# start()


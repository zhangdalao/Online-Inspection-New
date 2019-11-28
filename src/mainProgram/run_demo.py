# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import os, sys
import json
from flask import Flask
from src.common.runTest import sss

sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
sys.path.append(root_path)

import unittest
from src.common.BeautifulReport import BeautifulReport
from src.common.dingDing import send_link
from time import sleep
import socket
import time
from celery_once import QueueOnce
import platform
from src.common.configure_celery import configure_celery
from src.common.readConfData import GetDataIni

app = Flask(__name__)
celery = configure_celery(app)


def get_project_robot_URL(projectName=None):
	json_path = f"{root_path}{sep}data{sep}jsonFiles{sep}{projectName}.json"
	# 读取json数据文件中的内容
	with open(json_path, "r", encoding="utf-8") as j:
		json_data = json.load(j)
	return json_data


def get_cases(cases_dir, env, reg_str):
	"""
	:param cases_dir:    指定项目参数，根据指定的项目去获取用例,必填参数
	:param env:          指定运行环境
	:param reg_str
	:return:             返回指定项目的所有用例
	"""
	if not env:
		sss["env"] = "prod"
	elif env and env.lower() in ["dev", "test", "pre", "prod"]:
		sss["env"] = env
	
	# 判断是否有指定用例文件夹
	if cases_dir:
		project_dir = cases_dir  # test_xxxx
		# 获取指定项目的完整路径
		suites_dir = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + sep.join(['src', 'testProject',
		                                                                                          f'{project_dir}'])
	else:
		suites_dir = root_path + f'{sep}src{sep}testProject'
	# 获取本次需要执行的所有用例
	if not reg_str:
		reg_str = "*test.py"
	suite = unittest.defaultTestLoader.discover(start_dir=suites_dir, pattern=f'{reg_str}')
	return suite


@celery.task(base=QueueOnce)
def start(cases_dir, env, reg_str):
	# if not env:
	# 	sss["env"] = "prod"
	# elif env and env.lower() in ["dev", "test", "pre", "prod"]:
	# 	sss["env"] = env
	
	# 判断是否有指定用例文件夹
	if cases_dir:
		project_dir = cases_dir  # test_xxxx
		project_name = project_dir.split("test_")[-1]  # xxxx
		# 获取指定项目 json 数据中的 robot_url 的地址
		robot_url = get_project_robot_URL(project_name)[project_name]["robot_data"]["robot_url"]
	else:
		# 这里需要补充测试组机器人URL
		robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=d852c17cf61d26bfbaf8d0d8d4927632f9b1712cb9aa1' \
		            '45342159f8fd0065fc4'
		project_name = "All"
	
	suite = get_cases(cases_dir, env, reg_str)
	# print(suite.countTestCases())
	get_INI = GetDataIni()
	Name = get_INI.normal_data("Name", project_name)
	
	# 脚本运行当前时间
	now = time.strftime("%Y_%m_%d-%H_%M_%S")
	now_day = time.strftime("%Y_%m_%d")
	# 根据执行用例项目参数给测试报告命名
	reportFileName = f'{project_name}' + f'_{now}_result.html'
	
	# 测试报告存放文件夹地址
	reportDirName = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + 'output' + sep + 'report' + sep
	
	# 以天为维度生成对应文件夹
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
	
	# 根据第三方库 BeautifulReport 执行用例并生成报告
	with open(reportDir + sep + reportFileName, "wb"):
		beaRep = BeautifulReport(suite)
		res = beaRep.report(filename=reportFileName, description=f'{Name}项目 {env} 环境接口自动化测试报告',
		                    report_dir=reportDir)
		result_dict = beaRep.stopTestRun()
		casesAll = result_dict.get("testAll")
		casesPass = result_dict.get("testPass")
		casesFail = result_dict.get("testFail")
		# casesError = result_dict.get("testError")
		casesSkip = result_dict.get("testSkip")
		if not casesSkip:
			_pass_rate = ("%.2f%%" % (casesPass / casesAll * 100))
		else:
			_pass_rate = ("%.2f%%" % (casesPass / (casesAll - casesSkip) * 100))
		sleep(3)
		_platform = platform.platform()
		if _platform == 'Linux-2.6.32-754.18.2.el6.x86_64-x86_64-with-centos-6.10-Final':
			ip = '10.0.6.56'
			link_url = "http://" + ip + f':8686{sep}report{sep}{report_dir}{sep}{reportFileName}'
		elif _platform.startswith("Windows") or _platform.startswith('Darwin'):
			# 获取本机计算机名称
			hostname = socket.gethostname()
			# 获取本机ip
			ip = socket.gethostbyname(hostname)
			link_url = "http://" + ip + f':8686{sep}report{sep}{report_dir}{sep}{reportFileName}'
			robot_url = None
		else:
			ip = '10.50.255.253'
			output_dir = '/report/'
			link_url = "http://" + ip + f':1323{output_dir}{report_dir}{sep}{reportFileName}'
		if robot_url:
			send_link(robot_url, link_url, f'房多多接口自动化测试报告(通过率:{_pass_rate}) \n 用例总数:{casesAll}, '
			                                 f'通过:{casesPass},失败:{casesFail},跳过:{casesSkip}')
		return res

if __name__ == '__main__':
	# start('test_ddsf', 'test', "aa_login*")
	a = get_cases("test_ddsf", "test", "aa_login*")
	print(type(a.countTestCases()))

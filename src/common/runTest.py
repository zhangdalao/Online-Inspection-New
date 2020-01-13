# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-12


import unittest
from src.common.runMethod import RunMethod
from src.common.readLogger import ReadLogger
from jsonpath import jsonpath
import re
import json, time
from src.common.sign import SignKey
import os
from src.common.readConfData import GetDataIni
import traceback

sss = {}

sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))


# 定义断言函数(严格断言，字段类型和值必须一致)
def checkOut(res, exp) -> bool:
	"""
	:param res:        接口返回结果
	:param exp:        接口预期结果
	:return:           用于预期结果和实际结果断言，返回bool值
	"""
	for _key in exp:
		value = [_key, exp[_key]]
		check = jsonpath(res, expr=f"$..{value[0]}")
		if len(check) == 1 and check[0] == value[1]:
			pass
		elif len(check) > 1:
			check.__contains__(value[1])
			pass
		else:
			# print(f"断言失败！！！响应体中{_key}该字段的值为:{check[0]}，而预期结果为:{exp[_key]}")
			return False
	# print("断言成功！")
	return True


class RunTest(unittest.TestCase, unittest.SkipTest):
	def __init__(self, methodName='runTest'):
		super(RunTest, self).__init__(methodName)
		
		# 获取logger和run_log
		read_logger = ReadLogger()
		# 获取logger容器
		self.logger = read_logger.get_logger()
		# # 获取日志文件路径
		# self.run_log_src = read_logger.get_run_log()
		# 使用自封装requests
		self.method = RunMethod()
		self.desc = ""  # 用例描述
		self.api_name = ""  # 用例名称 api_name
		self.body = None  # 因为存在接口数据依赖原因，所以这里会单独申明body
		self.expect = None  # 后面需要日志打印预期结果
		self.desc = None
		self.result = None
		self.res = None
		self.projectName = None
		
		# 这里定义的 变量sss 作为全局变量在后面的
		global sss
	
	def skipTest(self, reason):
		"""
		过滤用例
		:param reason:  过滤用例原因
		:return:   unittest.SkipTest
		"""
		raise unittest.SkipTest
	
	def getCasePro(self):
		"""
		获取用例基本信息
		:return: desc
		"""
		data_ini = GetDataIni(f"{root_path}{sep}conf{sep}data.ini")
		if self.projectName:
			self.projectName = data_ini.normal_data("Name", self.projectName)
		else:
			self.projectName = "None"
		return self.projectName, self.api_name, self.desc
	
	def start(self, project, isSkip_num, apiName_num, url, method_num, headers_num, para_num, data_num, desc_num,
	          isRelate_num, expect_num, *args, **kw):
		"""
		用例运行主入口
		:param project:         项目名称
		:param isSkip_num:      是否跳过列数来判断该用例是否跳过执行
		:param apiName_num:     接口名称所在列数，获得接口名称
		:param url:             请求地址
		:param method_num:      请求方法所在列数
		:param headers_num      请求头所在列数
		:param para_num:        接口请求参数所在列数
		:param data_num:        接口请求体所在列数
		:param desc_num:        接口描述所在列数
		:param isRelate_num:    接口是否存在依赖参数所在列
		:param args:            从excle表中获取到的每条用例的测试数据
		:return:                API调用返回结果
		"""
		
		self.projectName = project
		isSkip = args[0][isSkip_num]
		self.api_name = args[0][apiName_num]
		method = args[0][method_num]
		isRelate = args[0][isRelate_num]
		self.desc = args[0][desc_num]
		# 这里需要保证 headers/params/body/断言结果 一定是字符串格式
		self.headers = str(args[0][headers_num]).strip()
		self.params = str(args[0][para_num]).strip()
		self.body = str(args[0][data_num]).strip()
		self.expect = str(args[0][expect_num]).strip()
		time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		
		# # 这里定义的 变量sss 作为全局变量在后面的
		# global sss
		
		# log日志中写入用例执行之前的一些接口基础数据
		self.logger.debug(f"项目名称         :{self.projectName}")
		self.logger.debug(f"用例名称         :{self.api_name}")
		self.logger.debug(f"用例描述         :{self.desc}")
		self.logger.debug(f"用例执行时间      :{time_str}")
		self.logger.debug(' 请求信息 '.center(80, '-'))
		
		# 判断用例是否执行
		if isSkip and str(isSkip).strip() == "是":
			self.logger.debug(f"是否跳过         :{isSkip}")
			self.skipTest('skip case')
			return False
		
		else:
			self.logger.debug("是否跳过         :否")
			self.logger.debug(f"用例请求方法      :{method}")
		# 用例不跳过时，按顺序执行代码
		try:
			# 定义替换字符
			re_str = '#\w+#'
			# 使用正则获取 host+path 中动态参数的字段列表
			re_list_uri = re.findall(re_str, url)
			# 最先替换 path 中动态参数，因为path + params 可能会参与加密
			if re_list_uri:
				for i in re_list_uri:
					i_value = sss.get(i[1:-1])
					if i_value:
						url = url.replace(i, str(i_value))
					else:
						self.logger.debug(f"***全局变量中缺少字段: {i[1:-1]}***")
			
			# 使用正则获取headers中参数化的字段列表
			re_list_header = re.findall(re_str, self.headers)
			# 使用正则获取params中参数化的字段列表
			re_list_params = re.findall(re_str, self.params)
			# 使用正则获取请求体中参数化的字段列表
			re_list_body = re.findall(re_str, self.body)
			# 使用正则获取预期结果(断言)中参数化的字段列表
			re_list_expect = re.findall(re_str, self.expect)
			if re_list_header:
				# 对headers中参数化的字段进行激活赋值
				for m in re_list_header:
					_str = f'data[\"{m[1:-1]}\"]'
					self.headers = self.headers.replace(m, _str)
			if re_list_params:
				# 对params中参数化的字段进行激活赋值
				for n in re_list_params:
					_str = f'data[\"{n[1:-1]}\"]'
					self.params = self.params.replace(n, _str)
			if re_list_body:
				# 对请求体中参数化的字段进行激活赋值
				for o in re_list_body:
					_str = f'data[\"{o[1:-1]}\"]'
					self.body = self.body.replace(o, _str)
			if re_list_expect:
				# 对预期结果中参数化的字段进行激活赋值
				for p in re_list_expect:
					_str = f'data[\"{p[1:-1]}\"]'
					self.expect = self.expect.replace(p, _str)
			# 将 sss 的值赋值给 data 变量
			data = sss
			# 先对 body/params/expect 做类型转换
			if self.body:
				self.body = eval(self.body)
			# 当存在 params 参数时，这里参数已经被激活处理，直接拼接在 host+path+params 得到准确 url
			if self.params:
				self.params = eval(self.params)
				for i in self.params.keys():
					if self.params[i] is None:
						self.params[i] = ''
				url = url + "?" + '&'.join(['{}={}'.format(*_) for _ in self.params.items()])
			if self.expect:
				self.expect = eval(self.expect)
			self.logger.debug(f"接口地址         :{url}")
		
			# 判断该接口是否有加密操作
			if type(args[0][-1]) == list:
				# 通过环境确定 url 中 host 后缀进行切割，从而拿到完整的 path
				suffix = {"test": ".net", "pre": ".com.cn", "prod": ".com"}
				path = url.split(suffix[sss["env"]])[-1]
				args[0][-1][-1] = path
				if self.body:
					# 对请求体中文转 json 后加密失败做处理
					args[0][-1].append(json.dumps(self.body))
				else:
					args[0][-1].append(str(self.body).replace("\'", '\"'))
				# 对其中的 path 存在动态参数进行解决
				for m in args[0][-1]:
					if m.__contains__('/') and re.findall(re_str, m):
						m_num = args[0][-1].index(m)
						uri_str_list = re.findall(re_str, m)
						for i in uri_str_list:
							i_value = sss.get(i[1:-1])
							if i_value:
								m = m.replace(i, str(i_value))
						args[0][-1][m_num] = m
				_str = ''.join(args[0][-1])
				data['sign_key'] = SignKey(_str).sign()
				args[0].pop()
			# try:
			if self.headers:
				# 对激活后的 headers做类型转换
				self.headers = eval(self.headers)
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			self.logger.debug(f"请求参数         :{self.params}")
			response = self.method.run_main(url, method, self.headers, self.body, **kw)
			self.res = response.json()
			self.logger.debug(f"响应结果         :{self.res}")
			self.logger.debug(f"预期结果         :{self.expect}")
		except KeyError as krr:
			error_value = str(krr)
			response = f"获取动态参数{error_value}失败!"
			self.logger.error(f"{response}")
			self.logger.error(f"报错信息         :{str(traceback.format_exc())}")
		# raise krr
		except ValueError as vrr:
			error_value = str(vrr)
			response = f"返回结果转换失败！  "
			self.logger.error(f'{response}')
			self.logger.error(f"返回结果为: {error_value} ")
			self.logger.error(error_value)
			self.logger.error(f"报错信息         :{str(traceback.format_exc())}")
		# raise vrr
		except TypeError as trr:
			error_value = str(trr)
			response = f"预期结果获取指定值失败！ {error_value}"
			self.logger.error(f'{response}')
			self.logger.error(f"报错信息         :{str(traceback.format_exc())}")
		# raise trr
		except Exception as err:
			error_value = str(err)
			response = f"请求时出现未知异常！  {error_value}"
			self.logger.error(f'{response}')
			self.logger.error(error_value)
			self.logger.error(f"报错信息         :{str(traceback.format_exc())}")
		# raise err
		else:
			if type(isRelate) == dict:
				relateData = isRelate.get("relateData")
				relateDatas = isRelate.get("relateDatas")
				# relateData = isRelate["relateData"]
				# 将需要提供依赖的数据缓存
				if relateData:
					for _dict in relateData:
						for _key in _dict:
							a = [_key, _dict[_key]]
							relate_value = jsonpath(self.res, expr=f"$..{a[0]}")
							if relate_value:
								# 这里如果 relate_value 存在的话类型其实是列表，所以取单个值使用需要注意
								sss[a[1]] = relate_value[0]
								self.logger.debug(f"依赖数据缓存成功    :{a[0]}-->{a[1]}, 数据值为:{relate_value[0]}")
							else:
								self.logger.debug("返回数据中指定的关联数据获取失败！")
				if relateDatas:
					for _dict in relateDatas:
						for _key in _dict:
							a = [_key, _dict[_key]]
							relate_value = jsonpath(self.res, expr=f"$..{a[0]}")
							if relate_value:
								# 这里如果 relate_value 存在的话类型其实是列表，所以取所有值使用需要注意
								sss[a[1]] = relate_value
								self.logger.debug(f"依赖数据缓存成功    :{a[0]}-->{a[1]}, 数据值为:{relate_value}")
							else:
								self.logger.debug("返回数据中指定的关联数据获取失败！")
		finally:
			return response
			
			# TODO  需要把断言封装详细一点，类型与值做区分

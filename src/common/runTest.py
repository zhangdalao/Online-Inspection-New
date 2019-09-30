# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-12


import unittest
from src.common.runMethod import RunMethod
from src.common.readLogger import ReadLogger
from jsonpath import jsonpath
import time
import re
import json
from src.common.sign import SignKey
import selenium


sss = {}


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


# 定义断言函数(模糊断言，字段类型不做要求，值必须相等)
def checkOut_withoutType(res, exp) -> bool:
	"""
	:param res:        接口返回结果
	:param exp:        接口预期结果
	:return:           用于预期结果和实际结果断言，返回bool值
	"""
	for _key in exp:
		value = [_key, exp[_key]]
		check = jsonpath(res, expr=f"$..{value[0]}")
		if len(check) == 1:
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
		self.req_msg = {'request': {}, '\nresponse': {}}  # 用例基本信息
	
	# 后面用例编号会使用
	
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
		return self.api_name, self.desc
	
	def start(self, isSkip_num, apiName_num, url, method_num, headers_num, para_num, data_num, desc_num, isRelate_num,
			  expect_num, *args, **kw):
		"""
		用例运行主入口
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
		
		# 这里定义的 变量sss 作为全局变量在后面的
		global sss
		
		# 先对 url 做处理
		re_str = '#\w+#'
		# 使用正则获取 uri 中参数化的字段列表
		re_list_uri = re.findall(re_str, url)
		if re_list_uri:
			for i in re_list_uri:
				i_value = sss.get(i[1:-1])
				if i_value:
					url = url.replace(i, str(i_value))
				else:
					self.logger.debug(f"***全局变量中缺少字段: {i[1:-1]}***")
		try:
			# log日志中写入用例执行之前的一些相关数据
			self.logger.debug(f"用例名称         :{self.api_name}")
			self.logger.debug(f"用例描述         :{self.desc}")
			self.logger.debug(f"用例执行时间      :{time_str}")
			self.logger.debug(' 请求信息 '.center(80, '-'))
			self.logger.debug(f"用例请求方法      :{method}")
			self.logger.debug(f"接口地址         :{url}")
		except Exception as e:
			self.logger.error('错误信息   : %s' % e)
		# 根据是否跳过参数判断用例是否执行
		if isSkip and isSkip != "否":
			self.logger.debug(f"是否跳过         :{isSkip}")
			self.skipTest('skip case')
		
		# 如果该接口关联类型只是关联输出
		# elif isRelate and isRelate["relateType"] == "relateOut":
		elif isRelate:
			relateData = isRelate["relateData"]
			self.logger.debug("是否跳过         :否")
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
					self.headers = self.headers.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
			if re_list_params:
				# 对headers中参数化的字段进行激活赋值
				for m in re_list_params:
					self.params = self.params.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
			if re_list_body:
				# 对请求体中参数化的字段进行激活赋值
				for n in re_list_body:
					self.body = self.body.replace(n, "f'{data[\"%s\"]}'" % (n[1:-1]))
			if re_list_expect:
				# 对预期结果中参数化的字段进行激活赋值
				for o in re_list_expect:
					self.expect = self.expect.replace(o, "f'{data[\"%s\"]}'" % (o[1:-1]))
			# 把全局变量赋值给 data 变量，数据类型为 dict
			data = sss
			# 先对 body/params 和预期结果做类型转换
			if self.body:
				self.body = eval(self.body)
			if self.params:
				self.params = eval(self.params)
			if self.expect:
				self.expect = eval(self.expect)
			if type(args[0][-1]) == list:
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
				print(_str)
				data['sign_key'] = SignKey(_str).sign()
				args[0].pop()
			# 最后对激活后的 headers 做类型转换
			self.headers = eval(self.headers)
			if re_list_header or re_list_body or re_list_expect or re_list_params:
				self.logger.debug("数据依赖类型      :需要依赖亦提供依赖数据")
			else:
				self.logger.debug("数据依赖类型      :无需依赖只提供依赖数据")
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			self.logger.debug(f"请求参数         :{self.params}")
			response = self.method.run_main(url, method, self.headers, self.params, self.body, **kw)
			# write_relate_json(data=res, relate_config=relateData)
			try:
				self.res = response.json()
				self.logger.debug(f"响应结果         :{self.res}")
				self.logger.debug(f"预期结果         :{self.expect}")
				# 将需要提供依赖的数据缓存
				for _dict in relateData:
					for _key in _dict:
						a = [_key, _dict[_key]]
						relate_value = jsonpath(self.res, expr=f"$..{a[0]}")
						if relate_value:
							# 这里如果 relate_value 存在的话类型其实是列表，所以取值使用需要注意
							sss[a[1]] = relate_value[0]
							self.logger.info(f"依赖数据缓存成功    :{a[0]}-->{a[1]}, 数据值为:{relate_value[0]}")
						else:
							self.logger.info("返回数据中指定的关联数据获取失败！")
						# print(sss)
			except Exception as err:
				self.logger.info(f" 实际结果为: {response} ")
				self.logger.error(str(err))
			return response
		# 如果该接口不用给其他接口提供依赖
		else:
			self.logger.debug("是否跳过         :否")
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
					self.headers = self.headers.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
					# print(self.headers)
					# print(type(self.headers))
			if re_list_params:
				# 对headers中参数化的字段进行激活赋值
				for m in re_list_params:
					self.params = self.params.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
			if re_list_body:
				# 对请求体中参数化的字段进行激活赋值
				for n in re_list_body:
					self.body = self.body.replace(n, "f'{data[\"%s\"]}'" % (n[1:-1]))
			if re_list_expect:
				# 对预期结果中参数化的字段进行激活赋值
				for o in re_list_expect:
					self.expect = self.expect.replace(o, "f'{data[\"%s\"]}'" % (o[1:-1]))
			data = sss
			# 先对 body/params 和预期结果做类型转换
			if self.body:
				self.body = eval(self.body)
			if self.params:
				self.params = eval(self.params)
			if self.expect:
				self.expect = eval(self.expect)
			if type(args[0][-1]) == list:
				# print(args[0][-1])
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
				print(_str)
				data['sign_key'] = SignKey(_str).sign()
				args[0].pop()
			# 对激活后的 headers做类型转换
			self.headers = eval(self.headers)
			if re_list_header or re_list_body or re_list_expect or re_list_params:
				self.logger.debug("数据依赖类型      :需要依赖但不提供依赖数据")
			else:
				self.logger.debug("数据依赖类型      :无依赖亦无提供依赖数据")
				
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			self.logger.debug(f"请求参数         :{self.params}")
			response = self.method.run_main(url, method, self.headers, self.params, self.body, **kw)
			try:
				self.res = response.json()
				self.logger.debug(f"响应结果         :{self.res}")
				self.logger.debug(f"预期结果         :{self.expect}")
			except Exception as err:
				self.logger.info(f" 实际结果为: {response} ")
				self.logger.error(str(err))
			# print(sss)
			return response
# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


"""基础类，封装requests常见7种请求方法"""

import requests


class MethodException(Exception):
	pass


class RunMethod(MethodException):
	
	headers_default = {"content-type": "application/json"}
	
	def run_main(self, url=None, method=None, headers=headers_default, para=None, data=None, **kw):
		
		"""
		封装常用的7种http请求方法
		:param method:        请求方法，从而获取请求方法 如 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD
		:param url:           请求url
		:param headers:       请求头，从而获取到请求头， 默认为 application/json
		:param para:          请求参数，从而获取到请求参数，默认 None
		:param data:          请求体数据，从而获取到请求体参数，默认 None
		:param kw:            其他参数
		:return:        Response object，type requests.Response
		# """
		#
		method_list1 = ["get", "delete", "head", "options"]
		method_list2 = ["post", "put", "patch"]

		try:
			if method and headers:
				if method.lower() in method_list1:
					res = requests.request(method.lower(), url, params=para, headers=headers, **kw)
				elif method.lower() in method_list2:
					if "application/json" in str(headers).lower():
						# post方法添加兼容json不传的情况, 并且兼用空字典，空列表等情况
						if not data and type(data) not in [list, dict, tuple, set]:
							res = requests.request(method.lower(), url, params=para, headers=headers, **kw)
						elif para:
							res = requests.request(method.lower(), url, params=para, json=data, headers=headers, **kw)
						else:
							res = requests.request(method.lower(), url, json=data, headers=headers, **kw)
					else:
						res = requests.request(method.lower(), url, params=para, data=data, headers=headers, **kw)
				else:
					print("Do Not Support Http Method!Please check the args of requests")
					raise MethodException
				return res
		except Exception as err:
			raise "接口请求数据获取失败！" + str(err)

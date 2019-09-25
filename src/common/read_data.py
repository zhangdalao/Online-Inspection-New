# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-01

import os
import json
import xlrd
import logging
from src.common.readLogger import ReadLogger
import re


class ReadData:
	def __init__(self, project=None, jsonName=None):
		"""
		:param project:    根据参数获得项目名称去读取excle中的sheet页，以及json中的数据, 默认为None
		:param project:    根据参数获得指定json文件名称，去读取对应json中的数据, 默认为None
		"""
		
		# 获取logger和run_log
		read_logger = ReadLogger()
		# 获取logger容器
		self.logger = read_logger.get_logger()
		self.logger.info(" 测试数据初始化 start! ".center(100, '='))
		sep = os.sep
		try:
			# 获得项目根目录
			root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
			self.logger.info(f"获取项目根目录正常 :{root_path}")
			# xlsx表格数据地址
			form_path = f"{root_path}{sep}data{sep}FDD接口测试用例.xlsx"
			self.logger.info(f"获取项目根正常          :{form_path}")
		
		# # 获得项目根目录
		# root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
		# # xlsx表格数据地址
		# form_path = f"{root_path}{sep}data{sep}FDD接口测试用例.xlsx"
		
			# 读取xlsx表格数据
			self.workbook = xlrd.open_workbook(form_path)  # 整个xlxs数据对象
			self.logger.info(f"读取xlsx表格数据正常:{self.workbook}")
			self.sheetNames = self.workbook.sheet_names()  # 页签名称列表
			self.logger.info(f"获取页签名称列表正常 :{self.sheetNames}")
			# 生成一个页签名称对应页签对象的字典
			self.form_data = {}
			for sheet in self.sheetNames:
				self.form_data[sheet] = self.workbook.sheet_by_name(sheet)
			self.logger.info(f"获取名称页签对象正常 :{self.form_data}")
			
			# 判断传入的项目名称是否有效
			if project and self.sheetNames.__contains__(project):
				self.pro = project
				self.logger.info(f"传入项目参数有效 :{self.pro}")
			else:
				print("\033[1;31m请确认【%s】名称是否正确或在表格中补充【%s】项目信息！！！\033[0m" % (project, project))
				self.logger.info(f"传入项目参数无效 :{project}")
		
			# 根据判断是否有传入jsonName进行json文件读取
			if jsonName:
				# json文件数据地址
				json_path = f"{root_path}{sep}data{sep}jsonFiles{sep}{jsonName}.json"
				self.logger.info(f"已传入json参数,其地址为  :{json_path}")
			else:
				# json文件数据地址
				json_path = f"{root_path}{sep}data{sep}config.json"
				self.logger.info(f"未传入json参数，默认地址为 :{json_path}")
				# 读取json数据文件中的内容
			with open(json_path, "r", encoding="utf-8") as j:
				self.json_data = json.load(j)
			self.logger.info(" 测试数据初始化 end! ".center(100, '='))
		except Exception as err:
			logging.error(" 测试数据文件读取出错! " + str(err))
			
	# 根据传入的项目名称获取表格中页签对象
	def get_sheetData(self) -> xlrd.sheet.Sheet:
		sheet_data = self.form_data[self.pro]
		return sheet_data
	
	# 根据表格数据获取列数据名称
	def get_titleData(self) -> list:
		Table_head_list = self.get_sheetData().row_values(0)
		return Table_head_list
	
	# 返回表格数据列表表头列数
	def row_Nums(self) -> int:
		num_rows = len(self.get_titleData())
		return num_rows
	
	# 根据传入表头名称返回对应的列数
	def get_num_name(self, title_name) -> int:
		"""
		:param title_name:          excle表头中的字段名称
		:return:                    excle表头中该字段所在列数
		"""
		for name in self.get_titleData():
			if title_name == name:
				return self.get_titleData().index(title_name)
	
	# 根据传入的表头名称参数返回一个字典对象：key-表头名称， value-列数
	def get_dict_name(self, title_name_list) -> dict:
		title_name_dict = {}
		for name in title_name_list:
			try:
				title_name_dict[name] = self.get_titleData().index(name)
			except Exception as er:
				print("\033[1;31m %s\033[0m" % str(er))
		return title_name_dict
		
	# 判断填写的表格数据是否符合规范
	def table_is_norm(self) -> bool:
		norm_list = ["环境", "模块名", "接口名称", "请求方法", "请求头", "请求参数", "用例描述", "请求体", "预期结果"]
		head_list = self.get_titleData()
		for title in norm_list:
			if not head_list.__contains__(title):
				print("\033[1;31m列表数据中缺乏 %s, 请在列表中补全相关数据！\033[0m" % title)
				return False
			else:
				pass
		return True
		
	# 根据传入的模块名称获取模块测试数据
	def get_module_data(self, fieldName=None) -> list:
		"""
		:param fieldName:          根据传入的模块名称筛选该模块的测试数据
		:return:                   返回该模块筛选出来的测试数据
		"""
		sheet_data = self.get_sheetData()
		fieldName_num = self.get_num_name("模块名")
		headers_num = self.get_num_name("请求头")
		body_num = self.get_num_name("请求体")
		para_num = self.get_num_name("请求参数")
		expect_num = self.get_num_name("预期结果")
		Table_data = []
		# 根据模块名fieldName把表格中的数据放在一起，后面如果有需要可以进行ddt
		for num in range(1, sheet_data.nrows):
			if sheet_data.row_values(num)[fieldName_num] == fieldName:
				row_data = []
				# 把每行数据中的 headers/body/断言结果 单独取出来
				special_data_list = [sheet_data.row_values(num)[headers_num], sheet_data.row_values(num)[body_num],
				                     sheet_data.row_values(num)[expect_num], sheet_data.row_values(num)[para_num]]
				for cell in sheet_data.row_values(num):
					if cell in special_data_list and cell:
						# 将 header/body/预期结果中的 json格式的特殊数据类型转换为Python支持的数据类型
						cell = cell.replace('null', 'None')
						cell = cell.replace('false', 'False')
						cell = cell.replace('true', 'True')
					try:
						cell = eval(cell)  # 这里做eval转换的目的是避免后期做，不然生成的报告中测试方法名称是一长串字符
					except Exception:
						pass
					row_data.append(cell)
				# print(f"row_data : {row_data}")
				# Table_data.append(sheet_data.row_values(num))
				Table_data.append(row_data)
		return Table_data
	
	# 根据传入的模块名称和接口名称过滤出需要的ddt测试数据
	def get_data_by_api(self, fieldName=None, api_name=None) -> list:
		"""
		:param fieldName:         模块名称，默认为None
		:param api_name:          接口名称，默认为None
		:return:                  根据模块名称和接口名称进行二次筛选，返回用于单个接口进行ddt的测试数据
		"""
		test_data_list = []
		# 根据传入的模块名称获取模块测试数据
		data = self.get_module_data(fieldName=fieldName)
		api_name_num = self.get_num_name("接口名称")
		for i in range(len(data)):
			if data[i][api_name_num] == api_name:
				test_data_list.append(data[i])
		return test_data_list
	
	# 根据传入的项目名称获取json中的机器人配置数据
	def get_robotData(self) -> dict:
		robotData = self.json_data[self.pro]["robot_data"]
		return robotData
	
	# 根据项目名称获取json中的domains列表，后面还需要根据环境获取特定的domain
	def get_domains(self):
		return self.json_data[self.pro]["domain"]
	
	# 根据传入的模块名，接口名返回接口路径，后面需要和domain去拼接
	def get_apiPath(self, fieldName=None, apiName=None):
		"""
		:param fieldName:         模块名称，默认为None
		:param apiName:           接口名称，默认为None
		:return:                  根据传入的模块名和接口名进行接口地址拼接，返回接口地址URL
		"""
		return self.json_data[self.pro][fieldName][apiName]
		# uri = self.json_data[self.pro][fieldName][apiName]
		# re_str = '#\w+#'
		# # 使用正则获取 uri 中参数化的字段列表
		# re_list_uri = re.findall(re_str, uri)
		# if re_list_uri:
		# 	uri_list_str = str(uri.split('/')).replace("\'#", "#")
		# 	uri_list_str = uri_list_str.replace("#\'", "#")
		# 	patch_list = re.findall(re_str, uri_list_str)
		# 	for m in patch_list:
		# 		uri_list_str = uri_list_str.replace(m, "f'{sss[\"%s\"]}'" % (m[1:-1]))
		# 	uri_list = eval(uri_list_str)
		# 	uri = '/'.join(uri_list)
		# # print(f"============uri==========:{uri}")
		# return uri
		
if __name__ == '__main__':
	a = ReadData("ddsf")
	# print(a.get_sheetData(), end='\n')
	# sheet = a.get_sheetData()
	# for i in range(0, sheet.nrows):
	# 	print(sheet.row_values(i))
	# b = a.get_titleData()
	# print(a.get_module_data("MapSource"))
	# print(a.get_num_name("用例名称"))
	# a.table_is_norm()
	# print(a.table_is_norm())
	# print(a.get_data_by_api("Login", "ByPassword"))
	# print(a.get_dict_name(["环境", "请求体", "预期结果1"]))
	print(a.get_module_data("Home"))
	# print(a.get_data_by_api("Login", "ByPassword"))
	# print(a.get_num_name("请求体"))
# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-12-09


import os
import xlrd


sep = os.sep


class CheckCases:
	
	def __init__(self, project=None, env=None):
		
		if project and project != "ALL":
			self.pro = project.split("test_")[-1]
		else:
			self.pro = "ALL"
		self.env = env
		root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
		# xlsx表格数据地址
		form_path = f"{root_path}{sep}data{sep}FDD接口测试用例.xlsx"
		# 读取xlsx表格数据
		self.workbook = xlrd.open_workbook(form_path)  # 整个xlxs数据对象
		self.sheetNames = self.workbook.sheet_names()  # 页签名称列表
		# 生成一个页签名称对应页签对象的字典
		self.form_data = {}
		for sheet in self.sheetNames:
			self.form_data[sheet] = self.workbook.sheet_by_name(sheet)
		
	# # 根据传入的项目名称获取表格中页签对象
	# def get_sheetData(self) -> xlrd.sheet.Sheet:
	# 	sheet_data = self.form_data[self.pro]
	# 	return sheet_data
		
	# 根据传入的项目名称获取表格中页签对象列表
	def get_sheetData_list(self) -> list:
		sheet_data_list = []
		if self.pro and self.sheetNames.__contains__(self.pro):
			sheet_data = self.form_data[self.pro]
			sheet_data_list.append(sheet_data)
		elif self.pro == "ALL":
			[sheet_data_list.append(i) for i in self.form_data.values()]
		return sheet_data_list
	
	# 根据表格数据获取列数据名称
	def get_titleData(self) -> list:
		Table_head_list = self.get_sheetData_list()[0].row_values(0)
		return Table_head_list
	
	# 根据传入表头名称返回对应的列数
	def get_num_name(self, title_name) -> int:
		"""
		:param title_name:          excle表头中的字段名称
		:return:                    excle表头中该字段所在列数
		"""
		for name in self.get_titleData():
			if title_name == name:
				return self.get_titleData().index(title_name)
	
	def check_cases(self):
		api_env_num = self.get_num_name("环境")
		data_list = self.get_sheetData_list()
		# for sheet in data_list:
		# 	env_data_set = set(sheet.sheet_author.ncols(api_env_num))
		new_data = map(lambda x: set(x.col_values(api_env_num)), data_list)
		new = list(new_data)
		# print(new)
		for i in new:
			if not i.__contains__(self.env):
				continue
			else:
				return True
			
	def counter_cases(self):
		cases_info_dict = {}
		if self.pro == "ALL":
			data_list = list(self.form_data.values())
		else:
			data_list = self.get_sheetData_list()
		if len(data_list) == 1:
			data_dict = {}
			api_name_num = self.get_num_name("接口名称")
			api_name_data = map(lambda x: set(x.col_values(api_name_num)), data_list)
			api_name_data_list = list(api_name_data)
			data_dict["api_name_count"] = len(api_name_data_list[0])
			cases_list_count = data_list[0].nrows - 1
			data_dict["cases_count"] = cases_list_count
			cases_info_dict[self.pro] = data_dict
		elif len(data_list) > 1:
			for k, v in self.form_data.items():
				data_dict = {}
				api_name_num = self.get_num_name("接口名称")
				api_name_data = map(lambda x: set(x.col_values(api_name_num)), [v])
				api_name_data_list = list(api_name_data)
				data_dict["api_name_count"] = len(api_name_data_list[0])
				cases_list_count = [v][0].nrows - 1
				data_dict["cases_count"] = cases_list_count
				cases_info_dict[k] = data_dict
		return cases_info_dict
		

if __name__ == '__main__':
	a = CheckCases("test_ddmf", "prod")
	# print(a.get_sheetData_list())
	print(a.check_cases())
	# a = CheckCases("ALL")
	# print(a.form_data)
	# # 统计用例条数及接口个数
	# a = CheckCases()
	# print(a.counter_cases())
	# api_count = 0
	# cases_count = 0
	# for i in a.counter_cases().items():
	# 	api_count += i[-1]["api_name_count"]
	# 	cases_count += i[-1]["cases_count"]
	# print(f"接口个数总计：{api_count}")
	# print(f"用例条数总计：{cases_count}")
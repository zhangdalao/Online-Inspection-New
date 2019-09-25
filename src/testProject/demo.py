# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-25


import re

sss = {"ID": 123456, "AGE": 23}

uri = '/login/home?name=#ID#&age=#AGE#'
uri1 = 'login/home/#ID#/user'
uri3 = ''

# re_str = '#\w+#'
# # 使用正则获取 uri 中参数化的字段列表
# re_list_uri = re.findall(re_str, uri)
# if re_list_uri:
# 	for i in re_list_uri:
# 		uri = uri.replace(i, str(sss[i[1:-1]]))
# 	# uri_list_str = str(uri.split('/')).replace("\'#", "#")
# 	# uri_list_str = uri_list_str.replace("#\'", "#")
# 	# patch_list = re.findall(re_str, uri_list_str)
# 	# for m in patch_list:
# 	# 	uri_list_str = uri_list_str.replace(m, "f'{sss[\"%s\"]}'" % (m[1:-1]))
# 	# print(uri_list_str)
# 	# # uri_list = eval(uri_list_str)
# 	# # uri = '/'.join(uri_list)


def replace(path):
	re_str = '#\w+#'
	# 使用正则获取 uri 中参数化的字段列表
	re_list_uri = re.findall(re_str, path)
	if re_list_uri:
		for i in re_list_uri:
			i_value = sss.get(i[1:-1])
			if i_value:
				path = path.replace(i, str(i_value))
			else:
				print("sss 却少字段！")
	return path

if __name__ == '__main__':
	print(replace(uri))

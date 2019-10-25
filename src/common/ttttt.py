#!/usr/bin/env python
# encoding: utf-8
'''
@author: fanpl
@file: ttttt.py
@time: 2019/10/12 16:40
@desc: 想练习一下读取并写入Excel
'''

import xlrd
import inspect


# book = xlrd.open_workbook("1111.xlsx")
#
# #返回一个xlrd.sheet.Sheet()对象,返回其中一个sheet 的所有数据
# table = book.sheet_by_name('ttopen')
#
# #返回sheet列表
# names = book.sheet_names()
#
# #根据sheet返回表头列名
# sheetlen = table.row_values(0)
#
# #输出列名在那一行
# lieming = '模块名'
# for i in sheetlen:
#     if lieming == i:
#         print(sheetlen.index(lieming))
#
# print(sheetlen.index('请求方法'))
#
#
# print(table)
# print(names)
# print(sheetlen)
# print(table.nrows)
#
# print("输出第一行数据信息: %s" %table.row_values(1))
#
# tt =[ table.row_values(1)[5],table.row_values(1)[6]]
# tt1 =[ table.row_values(2)[5],table.row_values(2)[6]]
#
# print(tt)
#
# pp = []
# pp.append(tt)
# pp.append(tt1)
# print(pp)



# def fanpenglitest():
#     print(type(inspect.stack()))
#     print(inspect.stack())
#     print(inspect.stack()[0][1])
# fanpenglitest()

#
# import os
# import json
# sep = os.sep
# root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
# jsonName = "ttopen"
# json_path = f"{root_path}{sep}data{sep}jsonFiles{sep}{jsonName}.json"
#
# with open(json_path,'r') as f:
#     json.data = json.load(f)
#
# print(json.data['ttopen']['domain']['pre'])
# print(json.data['ttopen'][''])


#
# import time
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'),time.localtime())



import re


# A='123456QWERT!@#$%\n' \
#   '<a> a<c>\n' \
#   '12s6634566666'
#
# com = re.findall(r'<.*>',A,re.S)
# print(com)
#
#
# re_str = '#\w+#'
#
# re_list_uri = re.findall(re_str,"https://ttopen.fangdd.net/api/#article#/list/#fetchArticleList#")
#
# print(type(re_list_uri))

# sss = {}
# def fddtest():
#     re_str = '#\w+#'
#     url = "https://ttopen.fangdd.net/api/#article#/list/#fetchArticleList#"
#     jsons = {"article":"#article#"}
#     re_list_uri = re.findall(re_str,j)
#
#     print(type(re_list_uri))
#     global sss
#
#     print(sss.get(1))
#     for i in re_list_uri:
#         i_value = sss.get(i[1:-1])
#         if i_value:
#              print(i_value)
#if __name__ == '__main__':
#     fddtest()
import json

data  = '{"name":"fdd"}'  null false


a = data["name"]
print(a)
# a = '#fanpl#'
# b = a.replace(a,"f'{data[%s]}'" % (a[1:-1]))
# print(b)
# a = 1
# b = [2, 3]
#
# def func():
#     global a
#     a = 2
#     print("in func a:", a)
#     b[0] = 1
#     print("in func b:", b)

# if __name__ == '__main__':
    # print("before func a:", a)
    # print("before func b:", b)
    # func()
    # print ("after func a:", a)
    # print ("after func b:", b)





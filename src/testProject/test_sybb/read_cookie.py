# -*- coding=utf-8 -*-
# Author: Zhou Cuiling
# @Date : 2019-10-18


import os


def readcookie():
    par_dir = os.path.dirname(__file__)
    sep = os.sep
    data_read=open(f'{par_dir}{sep}jgj_cookie.txt', "r")
    cookies=data_read.read()
    data_read.close()
    return cookies

if __name__ == '__main__':
    print(readcookie())
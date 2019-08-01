# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-24


import unittest
import requests


class TemplateTeseCase(unittest.TestCase):
	"""
	定义这个类的作用是给类定义个类变量：环境变量，这里作为开关，所有的用例的环境由这个参数决定
	"""
	env = "prod"
	s = requests.session()

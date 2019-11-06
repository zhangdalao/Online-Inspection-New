# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-11-06

import requests

url_login = 'https://ddsf.fangdd.com/ioux/loginByPassword/'
data_login = {"username": "18682236985", "password": "Wawa520."}

headers = {"content-type": "application/json"}

res_login = requests.post(url=url_login, headers=headers, json=data_login)
cookies = res_login.cookies
print(dir(cookies))

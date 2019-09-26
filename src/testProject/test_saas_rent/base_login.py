# coding=utf-8
import requests
import time
import re
import json
import os

global login_readconfig

# 云销系统登录获取cookie
def rent_saas_login():
    session = requests.session ()
    login_url="https://ddjj.fangdd.com/user/login"
    r = session.post (url=login_url,json={'mode': 1, 'userName': "18260421439", 'password': "123456"})
    cookie_value=requests.utils.dict_from_cookiejar(r.cookies)
    time.sleep(2)
    return cookie_value

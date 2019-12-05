# coding=utf-8
import requests
import time
import re
import json
import os

global login_readconfig

# 云销系统登录获取cookie
def rent_saas_login(environment):
    session = requests.session ()
    if environment=="prod":
        login_url="https://ddjj.fangdd.com/user/login"
        login_json={'mode': 1, 'userName': "18260421439", 'password': "123456"}
    elif environment=="pre":
        login_url = "https://ddjj.fangdd.com.cn/user/login"
        login_json = {'mode': 1, 'userName': "18260421439", 'password': "123456"}
    elif environment=="test":
        login_url = "https://ddjj.fangdd.net/user/login"
        login_json = {'mode': 1, 'userName': "18300000045", 'password': "111111"}
    r = session.post (url=login_url,json=login_json)
    cookie_value=requests.utils.dict_from_cookiejar(r.cookies)
    time.sleep(2)
    return cookie_value



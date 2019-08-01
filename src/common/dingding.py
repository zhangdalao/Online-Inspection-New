# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-07-31

import requests


# 推送钉钉消息调用方法（消息内容@手机号，手机号）
def send_ding(url, mobile, content=None):
    robot_url = url
    robot_body = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": mobile,
            "isAtAll": False
        }
    }
    r = requests.post(robot_url, json=robot_body)
    if r.status_code == 200:
        return True
    else:
        return False


# 钉钉推送测试报告调用方法（标题，内容，文件链接）
def send_link(tittle, text, url):
    robot_url = "https://oapi.dingtalk.com/robot/send?access_token=bd92a2ab1bd3243084849ffb96506e1620359581b97b49bafe870ba640b014c1"
    robot_body = {
        "msgtype": "link",
        "link": {
            "text": text,
            "title": tittle,
            "picUrl": "http://static.esf.fangdd.com/esf/factoringwebsiteesffdd/icon_fdd-1_tvW.svg",
            "messageUrl": url}
    }
    r = requests.post (robot_url, json=robot_body)
    if r.status_code == 200:
        return True
    else:
        return False

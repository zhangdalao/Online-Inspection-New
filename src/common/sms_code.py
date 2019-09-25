# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-23


import requests,re
import time

# 由于统一认证安全方面考量限制，登录用户名手机号需要是：13058019302，才可以调用该方法使用
def get_smsCode(env, send_code_url, method, **kw):
	if send_code_url and method:
		r = requests.request(method, url=send_code_url, **kw)
		if r.json()["code"] == 200 or 500:
			sms_url_dict = {
				"prod": 'http://sms.fangdd.cn/admin/api/verify-codes?mobile=13058019302',
				"pre": 'http://sms.fangdd.com.cn/admin/api/verify-codes?mobile=13058019302',
				"test": 'http://sms.fangdd.net/admin/api/verify-codes?mobile=13058019302'
			}
			sms_url = sms_url_dict[env]
			r = requests.get(sms_url)
			time.sleep(3)
			if r.json()["code"] == 0:
				# 获取短信内容
				sms_content = r.json()["records"]
				# 正则匹配出验证码内容
				print(sms_content)
				sms_code_list = re.findall("\d+", str(sms_content))
				# 获取最新的验证码
				sms_code = sms_code_list[0]
				# print(sms_code)
				return sms_code
			else:
				print("获取验证码失败！")
		else:
			print("触发验证码发送失败！")
	
	
if __name__ == '__main__':
	# r = requests.get("http://sms.fangdd.cn/admin/api/verify-codes?mobile=13058019302")
	# print(r.json())
	# get_smsCode("prod")
	a = get_smsCode("prod", 'https://shop.fangdd.com/api/boai/boai/user/authCode?mobile=13058019302&inUc=1', 'get')
	print(a)
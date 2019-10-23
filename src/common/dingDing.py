# coding=utf-8
import requests


# 推送钉钉消息调用方法（消息内容@手机号，手机号）
def send_ding(robotUrl, mobile, content=None, runType=None):
	"""
	:param robotUrl:          各个项目钉钉群内新增的机器人 url，必填参数
	:param mobile:            推送消息指定@对象，传入参数为 list对象，必填参数
	:param content:           推送消息内容，默认为None， 非必填
	:param runType:           运行类型，非必填，默认为None， 本地调式的话，这个参数需要自己传入，传入非None数据类型均可，如：1/'yes'/True
	:return:
	"""
	if robotUrl and content and mobile:
		# 巡检测试组机器人地址
		robot = 'https://oapi.dingtalk.com/robot/send?access_token=d852c17cf61d26bfbaf8d0d8d4927632f9b1712cb9aa145342159f8fd0065fc4'
		# 调试群机器人
		robot_test = 'https://oapi.dingtalk.com/robot/send?access_token=06fc833f73ad232ce00e5e2ee3d63ec299d72fd19fed82245cd6b083938f1616'
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
		if runType:
			# 当申明了非巡检执行时，则为本地调式模式，报错信息仅仅给调试机器人发送
			r = requests.post(robot_test, json=robot_body)
		# 非调试模式下，判断此时报错的群是不是巡检测试群
		elif str(robotUrl).strip() != robot:
			r = requests.post(robotUrl, json=robot_body)
			# 给巡检机器人测试组发送报错提示
			t = requests.post(robot, json=robot_body)
			if r.status_code == 200 and t.status_code == 200:
				return True
			else:
				return False


# 钉钉推送测试报告调用方法（标题，内容，文件链接）
def send_link(robot_url, result_path, tittle='测试报告', text='点击查看本次所有项目的测试用例执行详情'):
	"""
	:param robot_url:          各个项目钉钉群内新增的机器人 url，必填参数
	:param result_path:        项目测试结果报告路径，必填参数
	:param tittle:             推送测试报告链接 title，默认为None
	:param text:               测试报告简介内容，默认为None
	:return:
	"""
	# robot_url = "https://oapi.dingtalk.com/robot/send?access_token
	# =bd92a2ab1bd3243084849ffb96506e1620359581b97b49bafe870ba640b014c1"
	# url = robot_url,
	# url = 'https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf' \
	#             '2b498bcece2644a'
	robot_body = {
		"msgtype": "link",
		"link": {
			"text": text,
			"title": tittle,
			"picUrl": "http://static.esf.fangdd.com/esf/factoringwebsiteesffdd/icon_fdd-1_tvW.svg",
			"messageUrl": result_path}
	}
	r = requests.post(robot_url, json=robot_body)
	if r.status_code == 200:
		return True
	else:
		return False


if __name__ == '__main__':
	
	robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf' \
				'2b498bcece2644a'
	result_path = 'http://localhost:63342/api_automate_test/output/report/report_2019_09_11-17_14_43/2019_09_11-17_' \
				  '14_43_result.html'
	# print(send_ding(robot_url, ["18682236985", "17770035302", "15890608240"], "糟糕出错啦！"))
	print(send_link(robot_url, result_path))
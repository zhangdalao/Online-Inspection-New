# coding=utf-8
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkdyvmsapi.request.v20170525.SingleCallByTtsRequest import SingleCallByTtsRequest
from src.common.runTest import sss


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
		robot = 'https://oapi.dingtalk.com/robot/send?access_token=d852c17cf61d26bfbaf8d0d8d4927632f9b1712cb9aa14534' \
		        '2159f8fd0065fc4'
		# 调试群机器人
		robot_test = 'https://oapi.dingtalk.com/robot/send?access_token=06fc833f73ad232ce00e5e2ee3d63ec299d72fd19fed' \
		             '82245cd6b083938f1616'
		robot_body = {
			"msgtype": "text",
			"text": {
				"content": f"【{sss['env_name']}】"+content
			},
			"at": {
				"atMobiles": mobile,
				"isAtAll": False
			}
		}
		# 判断如果本地调试模式或者运行环境为测试环境只会往调试群发告警
		if runType or sss["env_name"] in ["test", "pre", "prod"]:
			requests.post(robot_test, json=robot_body)
		# 非调试模式下，判断此时报错的群是不是巡检测试群
		elif str(robotUrl).strip() != robot:
			try:
				requests.post(robotUrl, json=robot_body)
				# 给巡检机器人测试组发送报错提示
			except Exception:
				pass
			finally:
				num = 0
				# 如果失败尝试调用3次
				while num < 3:
					t = requests.post(robot, json=robot_body)
					num += 1
					if t.status_code == 200:
						break
					
					
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


# 报警电话调用方法 (**慎用**只限于线上环境核心业务！！)
def makeCall(phoneNum, env=None):
	"""
	:param phoneNum:        需要通知人的电话号码，必填参数  字符串格式
	:param env:             环境，必须是线上环境才支持电话警告
	:return:
	"""
	
	if env == "prod" and phoneNum.isdigit() and len(phoneNum) == 11:
		accessKeyId = "LTAI4FpbudWJvDGc1N9TZ5Q9"
		accessSecret = "IbSPM3X2l6Ldq06rKy35NQVebQabYc"
		
		client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')
		
		request = SingleCallByTtsRequest()
		request.set_accept_format('json')
		
		request.set_CalledShowNumber("055162153901")
		request.set_CalledNumber(phoneNum)
		request.set_TtsCode("TTS_179160339")
		
		response = client.do_action_with_exception(request)
		# python2:  print(response)
		# print(str(response, encoding='utf-8'))
		return str(response, encoding='utf-8')
	else:
		return "参数有误，报警电话暂只支持线上环境核心业务！"
	

if __name__ == '__main__':
	
	# robot_url = 'https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf' \
	# 			'2b498bcece2644a'
	# result_path = 'http://localhost:63342/api_automate_test/output/report/report_2019_09_11-17_14_43/2019_09_11-17_' \
	# 			  '14_43_result.html'
	# # print(send_ding(robot_url, ["18682236985", "17770035302", "15890608240"], "糟糕出错啦！"))
	# print(send_link(robot_url, result_path))
	res = makeCall("18682236985", "prod")
	print(res)
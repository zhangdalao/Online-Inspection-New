from flask import Flask, request, jsonify, Response

from src.mainProgram.run import get_cases, start
# from src.mainProgram.run_demo import start, get_cases
from src.common.readConfData import GetDataIni
from configparser import *
import json


app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/run_test", methods=["post"])
def run_test():
	try:
		data_dict = json.loads(request.get_data())
		# 从请求中获取请求参数
		cases_names = data_dict.get('cases')
		env_name = data_dict.get('env')
		reg_str = data_dict.get("reg_str")
		dataIni = GetDataIni()
		# 检查必填参数是否填写
		if cases_names and env_name:
			cases = dataIni.normal_data("Project_name", cases_names)  # test_ddsf/ALL
			env = dataIni.normal_data("Env_name", env_name)           # prod
			if cases == "ALL":
				cases = None
			suite_num = get_cases(cases, env, reg_str).countTestCases()
			if suite_num == 0:
				res = jsonify({"code": 201, "success": False, "cases_count": suite_num, "msg": "请确认参数，获取用例失败!"})
			else:
				start.delay(cases_dir=cases, env=env, reg_str=reg_str)
				res = jsonify({"code": 200, "success": True, "cases_count": suite_num,
				               "msg": f"{cases_names}项目{env_name}环境 自动化测试正在执行，请注意查收钉钉推送消息"})
		else:
			res = jsonify({"code": 10000, "success": False, "msg": "缺少必填参数！"})
	except NoOptionError:
		res = jsonify({"code": 10001, "success": False, "msg": "自动化测试执行失败！请求参数解析出错！"})
	except Exception:
		res = jsonify({"code": 10002, "success": False, "msg": "自动化测试执行失败! 出现未知错误！"})
	return res


@app.route("/run_test/<path:cases_list>", methods=["get"])
def get_projects(cases_list):
	if cases_list.split('/')[-1] == "cases_list":
		dataIni = GetDataIni()
		names_list = dataIni.cfgB.options("Project_name")
		res = json.dumps(names_list, ensure_ascii=False)
		return Response(res, mimetype="application/json")

# @app.route("/start_test", methods=["post"])
# def start_test():
#     cases = request.form.get("cases")
#     env = request.form.get("env")
#     a = s_demo.delay(cases_dir=cases, env=env)
#     return jsonify(a)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1322)


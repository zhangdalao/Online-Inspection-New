from flask import Flask, request, jsonify, Response
from flask_cors import *
from src.mainProgram.run import start
# from src.mainProgram.run_demo import start, get_cases
from src.common.readConfData import GetDataIni
from configparser import *
import json
from src.common.checkCases import CheckCases


app = Flask(__name__)
# CORS(app, resources={r"/.*": {"origins": "*.fangdd.net"}})
CORS(app, resources=r"/*")


@app.route("/", methods=["get", "post"])
def hello():
	return "Hello, World!"


@app.route("/cases_list", methods=["get", "post", "options"])
def get_projects():
	dataIni = GetDataIni()
	names_list = dataIni.cfgB.options("Project_name")
	res = json.dumps(names_list, ensure_ascii=False)
	return Response(res, mimetype="application/json")


@app.route("/env_list", methods=["get", "post", "options"])
def get_env():
	dataIni = GetDataIni()
	names_list = dataIni.cfgB.options("Env_name")
	res = json.dumps(names_list, ensure_ascii=False)
	return Response(res, mimetype="application/json")


@app.route("/env_name_json", methods=["get", "post", "options"])
def get_env_name_json():
	dataIni = GetDataIni()
	method = request.method.lower()
	if method == "get":
		param = request.args.get("envId")
	else:
		param = str(json.loads(request.get_data()).get("envId"))
	if dataIni.cfgB.options("Env_name").__contains__(param):
		env_name = eval(dataIni.normal_data("Env_name", param))[-1]
		res = {"msg": True, "options": param, "env_name": env_name}
	else:
		res = {"msg": f"The <envId={param}> is invalid!"}
	response = json.dumps(res, ensure_ascii=False)
	return Response(response,  mimetype="application/json")


@app.route("/env_name_url_form", methods=["get", "post", "options"])
def get_env_name_url_form():
	dataIni = GetDataIni()
	method = request.method.lower()
	if method == "get":
		param = request.args.get("envId")
	else:
		param = str(request.form.get("envId"))
	if dataIni.cfgB.options("Env_name").__contains__(param):
		env_name = eval(dataIni.normal_data("Env_name", param))[-1]
		res = {"msg": True, "options": param, "env_name": env_name}
	else:
		res = {"msg": f"The <envId={param}> is invalid!"}
	response = json.dumps(res, ensure_ascii=False)
	return Response(response,  mimetype="application/json")


@app.route("/run_test", methods=["post", "options"])
def run_test():
	try:
		data_dict = json.loads(request.get_data())
		# 从请求中获取请求参数
		cases_names = data_dict.get('cases')   # "多多商服/全部/多多新房"
		env_num = data_dict.get('env')        # 1 ->int
		reg_str = data_dict.get("reg_str")
		dataIni = GetDataIni()
		# 检查必填参数是否填写
		if cases_names and env_num:
			cases = dataIni.normal_data("Project_name", cases_names)  # test_ddsf/ALL
			# 前端传过来的是 int 类型，INI配置文件中是默认为字符串的，需要处理下
			env_data = eval(dataIni.normal_data("Env_name", str(env_num)))          # ["prod", "正式环境"]  -> list
			
			if cases == "test_ddxf":
				# check = True
				check_shop = CheckCases("test_shop", env_data[0]).check_cases()
				check_shopapp = CheckCases("test_shopapp", env_data[0]).check_cases()
				check_ddxfapp = CheckCases("test_ddxfapp", env_data[0]).check_cases()
				check = check_shop or check_ddxfapp or check_shopapp
			else:
				check = CheckCases(cases, env_data[0]).check_cases()
			if not check:
				res = jsonify({"code": 201, "success": False, "cases_count": 0, "msg": "请确认参数，获取用例失败!"})
			else:
				# start.delay(cases_dir=cases, env=env_data[0], reg_str=reg_str)
				# 尝试修复环境参数经过函数 delay 丢失的bug
				start.apply_async(args=[cases, env_data[0], reg_str])
				res = jsonify({"code": 200, "success": True, "msg": f"{cases_names}项目{env_data[1]}环境 "
				                                                    f"自动化测试正在执行，请注意查收钉钉推送消息"})
		else:
			res = jsonify({"code": 10000, "success": False, "msg": "缺少必填参数！"})
	except NoOptionError:
		res = jsonify({"code": 10001, "success": False, "msg": "自动化测试执行失败！请求参数解析出错！"})
	except Exception:
		res = jsonify({"code": 10002, "success": False, "msg": "自动化测试执行失败! 出现未知错误！"})
	return res


# @app.route("/start_test", methods=["post"])
# def start_test():
#     cases = request.form.get("cases")
#     env = request.form.get("env")
#     a = s_demo.delay(cases_dir=cases, env=env)
#     return jsonify(a)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=65387, debug=True)


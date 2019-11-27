from flask import Flask, request, jsonify

from src.mainProgram.run import start
from src.common.readConfData import GetDataIni
from configparser import *


app = Flask(__name__)


@app.route("/")
def hello():
	return "Hello, World!"


@app.route("/run_test")
def run_test():
	try:
		cases = request.args.get('cases', None)
		env = request.args.get('env', None)
		dataIni = GetDataIni()
		project = cases.split("test_")[-1]
		p_name = dataIni.normal_data("Name", project)
		e_name = dataIni.normal_data("Env", str(env))
		if cases == "All":
			cases = None
		start.delay(cases_dir=cases, env=env)
	except NoOptionError:
		res = jsonify({"code": 10001, "success": False, "msg": "自动化测试执行失败！请求参数不存在"})
	except Exception:
		res = jsonify({"code": 10002, "success": False, "msg": "自动化测试执行失败! 出现未知错误！"})
	except ZeroDivisionError:
		res = jsonify({"code": 10011, "success": True, "msg": "自动化测试结束！根据指定参数未获取到用例！"})
	else:
		res = jsonify({"code": 200, "success": True, "msg": f"{p_name}项目{e_name}环境自动化测试已启动,请耐心等待钉钉推送执行结果！"})
	return res


# @app.route("/start_test", methods=["post"])
# def start_test():
#     cases = request.form.get("cases")
#     env = request.form.get("env")
#     a = s_demo.delay(cases_dir=cases, env=env)
#     return jsonify(a)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1322)


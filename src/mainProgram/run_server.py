from flask import Flask, request, jsonify

from src.mainProgram.run import start
from src.mainProgram.run_demo import start as s_demo

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


# @app.route("/run_test")
# def run_test():
#     cases = request.args.get('cases',None)
#     env = request.args.get('env',None)
#     start.delay(cases_dir=cases, env=env)
#     return "自动化测试已启动"


@app.route("/run_test")
def run_test():
    cases = request.args.get('cases', None)
    env = request.args.get('env', None)
    a = start.delay(cases_dir=cases, env=env)
    if a["code"] == 200:
        return jsonify({"code": 200, "msg": "自动化测试已成功执行结束！"})


# @app.route("/start_test", methods=["post"])
# def start_test():
#     cases = request.form.get("cases")
#     env = request.form.get("env")
#     a = s_demo.delay(cases_dir=cases, env=env)
#     return jsonify(a)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1322)


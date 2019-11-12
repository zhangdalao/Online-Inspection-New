from flask import Flask, request

from src.mainProgram.run import start

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/run_test")
def run_test():
    cases = request.args.get('cases',None)
    env = request.args.get('env',None)
    start.delay(cases_dir=cases, env=env, kwarg1='cases_dir',kwarg2='env')
    return "自动化测试已启动"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1322)


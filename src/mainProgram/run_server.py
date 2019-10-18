from flask import Flask

from src.mainProgram.run import start

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/run_test")
def run_test():
    start.delay()
    return "自动化测试已启动"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1322)


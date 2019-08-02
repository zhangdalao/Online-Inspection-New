# coding=utf-8
import sys, os
import logging
import datetime
from logging.handlers import RotatingFileHandler

# 获取logger实例，如果参数为空则返回root logger
logger_info = logging.getLogger("infoLog")
logger_error = logging.getLogger("errorLog")

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s')

# 设置文件路径和时间(timedelta：多少天之前配置)
curDate = datetime.date.today() - datetime.timedelta(days=0)


# grandpa_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
grandpa_path = os.path.abspath(os.path.join(__file__, "../../.."))

infoLogName = r'%s/output/logs/info_%s.log' % (grandpa_path, curDate)
errorLogName = r'%s/output/logs/error_%s.log' % (grandpa_path, curDate)


# 文件日志:最多备份5个日志文件，每个日志文件最大10M
# file_handler_info = logging.FileHandler(infoLogName)
file_handler_info = RotatingFileHandler(infoLogName, maxBytes=10 * 1024 * 1024, backupCount=5)
file_handler_info.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

file_handler_error = RotatingFileHandler(errorLogName, maxBytes=10 * 1024 * 1024, backupCount=5)
file_handler_error.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger_info.addHandler(file_handler_info)
logger_info.addHandler(console_handler)

logger_error.addHandler(file_handler_error)
logger_error.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger_info.setLevel(logging.INFO)
logger_error.setLevel(logging.ERROR)

# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-23


"""基础类，用于读取日志配置和和获取日志文件"""
import os
import logging
import logging.config
import time

sep = os.sep


class ReadLogger:
    
    def __init__(self):
        """ 读取日志配置 """
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 项目根路径
        # root_dir = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))  # 项目根路径
        # print(root_dir)
        logConfFileName = 'logs.conf'  # 指定日志配置文件名称
        logConfFilePath = root_dir + sep + 'conf' + sep + logConfFileName  # 指定日志配置文件绝对路径
        now_day = time.strftime("%Y_%m_%d")
        runLogPath = f'{root_dir}{sep}output{sep}logs{sep}{now_day}'
        if not os.path.exists(runLogPath):
            os.mkdir(runLogPath)
        logging.config.fileConfig(logConfFilePath, defaults={"LogPath": runLogPath})
        self.logger = logging.getLogger(name='rotatingFileLogger')

    def get_logger(self):
        """ 获取logger容器 """
        return self.logger
    

if __name__ == "__main__":
    read_logger = ReadLogger()
    logger = read_logger.get_logger()
    logger.debug('debug message')

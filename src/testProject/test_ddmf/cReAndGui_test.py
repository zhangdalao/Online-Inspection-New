# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08

import random
import datetime
from datetime import timedelta
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import *
import urllib3

count = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@ddt.ddt
class ReAndGuiTest(RunTest):
    """新房报备带看模块"""

    # 通过文件名夹获取project参数的值
    project = os.path.dirname(__file__)[-4:]
    # 读取文件实例化
    a = ReadData(project, project)
    # 通过类名获取fieldname的值
    fieldname = sys._getframe().f_code.co_name[:-4]
    # 获取项目名后，获取机器人相关配置
    json_dict = a.json_data[project]["robot_data"]
    robot_url = json_dict["robot_url"]
    mobile = json_dict["mobile"]

    @classmethod
    def setUpClass(cls):
        cls.env_num = cls.a.get_num_name("环境")
        cls.apiName_num = cls.a.get_num_name("接口名称")
        cls.method_num = cls.a.get_num_name("请求方法")
        cls.headers_num = cls.a.get_num_name("请求头")
        cls.para_num = cls.a.get_num_name("请求参数")
        cls.desc_num = cls.a.get_num_name("用例描述")
        cls.data_num = cls.a.get_num_name("请求体")
        cls.expect_num = cls.a.get_num_name("预期结果")
        cls.isSkip_num = cls.a.get_num_name("是否跳过该用例")
        cls.relateData_num = cls.a.get_num_name("接口关联参数")
        t = time.time()
        cls.timestamp = str(round(t * 1000))
        guidetime = datetime.datetime.now() + timedelta(hours=1)
        cls.GuideTime = guidetime.strftime("%Y-%m-%d %H:%M:%S")
        phone_num = random.randint(00000000, 99999999)
        cls.phone_num = '199' + str(phone_num)
        # 前三后四
        hidephone = random.randint(0000, 9999)

        # 前九后二
        hidephone1 = random.randint(000000000, 999999999)

        # 前五后二
        hidephone2 = random.randint(00000, 99999)
        cls.hidephone = '199' + '****' + str(hidephone)
        cls.hidephone1 = str(hidephone1) + '**'
        cls.hidephone2 = str(hidephone2) + '****' + '99'
        sss["timestamp"] = cls.timestamp
        sss["GuideTime"] = cls.GuideTime
        sss["phonenum"] = cls.phone_num
        sss["hidephone"] = cls.hidephone
        sss["hidephone1"] = cls.hidephone1
        sss["hidephone2"] = cls.hidephone2

    def setUp(self):
        globals()['count'] += 1
        self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))

    def tearDown(self):
        if self.result and type(self.result) != str:
            try:
                self.assertEqual(True, checkOut(self.res, self.expect))
                self.logger.debug("测试结果         :测试通过！")
            except Exception as err:
                self.logger.error("测试结果         :测试失败！")
                send_ding(self.robot_url, self.mobile,
                          content=f"{self.desc}测试失败！\n接口返回为：{self.res}, 预期结果为：{self.expect}")
                if self.apiName in ["batchreferral", "guide"]:   # 当报错时，判断是不是报备或者带看接口，是的话需要语音报警
                    makeCall(self.mobile[0], sss["env"])
                raise err
        elif self.result and type(self.result) == str:
            send_ding(self.robot_url, self.mobile, content=f"{self.desc}测试失败！\n测试反馈:{self.result}")
            raise Exception
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "trianglelist"))
    def test_trianglelist(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "triangledetail"))
    def test_triangledetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "re_rule"))
    def test_re_rule(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "batchreferral"))
    def test_batchreferral(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "guide"))
    def test_guide(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["triangleId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "upcert"))
    def test_upcert(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["guideId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

if __name__ == '__main__':
    unittest.main()
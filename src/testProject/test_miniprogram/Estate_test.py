# -*- coding=utf-8 -*-
# Author: Yuan Luo
# @Date : 2019-10-11


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding

count = 0


@ddt.ddt
class EstateTest(RunTest):
    """首页相关测试用例"""

    # 获取当前文件路径
    project = os.path.dirname(__file__)[-11:]
    # 读取xls中对应的列
    a = ReadData(project, "miniprogram")
    # 通过类名获取模块名
    fieldname = sys._getframe().f_code.co_name[:-4]
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
        sss["timestamp"] = cls.timestamp

    def setUp(self):
        globals()['count'] += 1
        self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))

    def tearDown(self):
        if self.result and type(self.result) != str:
            try:
                self.assertEqual(True, checkOut(self.res, self.expect))
                self.logger.debug("测试结果         :测试通过！")
            except Exception as err:
                print(sss["env"])
                self.logger.error("测试结果         :测试失败！")
                send_ding(self.robot_url, self.mobile,
                          content=f"【{sss['env']}环境】 {self.desc}测试失败！\n接口返回为：{self.res}, 预期结果为：{self.expect}")
                raise err
        elif self.result and type(self.result) == str:
            send_ding(self.robot_url, self.mobile, content=f"【{sss['env']}】环境 {self.desc}测试失败！\n测试反馈:{self.result}")
            raise Exception
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    # @ddt.data(*a.get_data_by_api(fieldname, "EstateList"))
    # def test_EstateList(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName)
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     print(self.headers_num)
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False, timeout=10)


    # @ddt.data(*a.get_data_by_api(fieldname, "EstateSearch"))
    # def test_EstateSearch(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName)
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     print(self.headers_num)
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
    #                      timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "EstateCustList"))
    def test_EstateCustList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "UnreadMsgNums"))
    def test_UnreadMsgNums(self, value):
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
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CommissionsList"))
    def test_CommissionsList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CustList"))
    def test_CustList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideList"))
    def test_GuideList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "RefreList"))
    def test_RefreList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderList"))
    def test_OrderList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CustSearch"))
    def test_CustSearch(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    # @ddt.data(*a.get_data_by_api(fieldname, "CustDetail"))
    # def test_CustDetail(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["custId"])+"/detail"
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     print(self.headers_num)
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
    #                      timeout=10)

    # @ddt.data(*a.get_data_by_api(fieldname, "GuideApply"))
    # def test_GuideApply(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["userId"]) + "/"+str(sss["triangleId"])
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     print(self.headers_num)
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
    #                      timeout=10)

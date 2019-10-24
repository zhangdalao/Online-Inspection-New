# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
import requests
from src.common.dingDing import send_ding
from src.testProject.test_saas_rent.base_login import rent_saas_login

count = 0


@ddt.ddt
class Rent_TradeTest(RunTest):
    """房源列表模块"""

    # 通过文件名夹获取project参数的值
    project = os.path.dirname(__file__)[-9:]
    print(project)
    # 读取文件实例化
    a = ReadData(project, 'saas_rent')
    # 通过类名获取fieldname的值
    fieldname = sys._getframe().f_code.co_name[:-4]
    print(fieldname)

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
        cls.cookie_txt = rent_saas_login()

    def setUp(self):
        globals()['count'] += 1
        self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))

    def tearDown(self):
        if self.result:
            try:
                self.assertEqual(True, checkOut(self.res, self.expect))
                self.logger.debug("测试结果         :测试通过！")
            except Exception as err:
                self.logger.error("测试结果         :测试失败！")
                json_dict = self.a.json_data[self.project]["robot_data"]
                robot_url = json_dict["robot_url"]
                mobile = json_dict["mobile"]
                send_ding(robot_url, mobile, content=f"{self.desc}测试失败！接口返回为：{self.res}, 接口预期结果为：{self.expect}")
                raise err
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "get_RentTradeList"))  # 接口对应的名称
    def test_01_get_RentTradeList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        print("请求体的数据为：", self.data_num)
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)

    @ddt.data(*a.get_data_by_api(fieldname, "create_RentTrade"))  # 接口对应的名称
    def test_02_create_RentTrade(self, value):

        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        sss["signTime"] = int(time.time()) * 1000
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)
        sss["restful_trade"] = json.dumps({"tradeId": sss["ID8"]})
        time.sleep(2)

    @ddt.data(*a.get_data_by_api(fieldname, "get_RentTradeDetail"))  # 接口对应的名称
    def test_03_get_RentTradeDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)

    @ddt.data(*a.get_data_by_api(fieldname, "confirm_RentAchievement"))  # 接口对应的名称
    def test_04_confirm_RentAchievement(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)

    @ddt.data(*a.get_data_by_api(fieldname, "create_ShouldReceive"))  # 接口对应的名称
    def test_05_create_ShouldReceive(self, value):
        """录入租房应收单"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)
        sss["restful_HasReceived"] = json.dumps({"tradeId": sss["ID8"], "receivableId": sss["ID9"]})
        time.sleep(2)


    @ddt.data(*a.get_data_by_api(fieldname, "create_HasReceived"))  # 接口对应的名称
    def test_06_create_HasReceived(self, value):
        """录入租房实收单"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)


    @ddt.data(*a.get_data_by_api(fieldname, "create_ShouldPay"))  # 接口对应的名称
    def test_07_create_ShouldPay(self, value):
        """录入租房应付单"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)
        sss["restful_HasPaid"] = json.dumps({"tradeId": sss["ID8"], "payableId": sss["ID10"]})
        time.sleep(2)

    @ddt.data(*a.get_data_by_api(fieldname, "create_HasPaid"))  # 接口对应的名称
    def test_08_create_HasPaid(self, value):
        """录入租房实付单"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)

    @ddt.data(*a.get_data_by_api(fieldname, "close_RentTrade"))  # 接口对应的名称
    def test_09_close_RentTrade(self, value):
        """结案租房交易单"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)

    @ddt.data(*a.get_data_by_api(fieldname, "add_CustomerGuide"))  # 接口对应的名称
    def test_10_add_CustomerGuide(self, value):
        """录入租房带看成功"""
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[8:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                         cookies=self.cookie_txt)


if __name__ == '__main__':
    unittest.main()
# -*- coding=utf-8 -*-
# Author: Yuan Luo
# @Date : 2019-10-09


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding

count = 0


@ddt.ddt
class H5Test(RunTest):
    """H5相关用例"""

    project = os.path.dirname(__file__)[-7:]
    a = ReadData(project, project)
    fieldname = sys._getframe().f_code.co_name[:-4]

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

    @ddt.data(*a.get_data_by_api(fieldname, "StoreRange"))
    def test_StoreRange(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "LayoutList"))
    def test1_LayoutList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "LayoutDetail"))
    def test2_LayoutDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "LayoutEdit"))
    def test3_LayoutEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuantityDtail"))
    def test1_QuantityDtail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuantityEdit"))
    def test2_QuantityEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueList"))
    def test_ClueList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueAdd"))
    def test_ClueAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueOperationData"))
    def test_ClueOperationData(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueRealtorDayList"))
    def test_ClueRealtorDayList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueRealtorWeekList"))
    def test_ClueRealtorWeekList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ClueRealtorMonList"))
    def test_ClueRealtorMonList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "AddRealtorRecord"))
    def test_AddRealtorRecord(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)


if __name__ == '__main__':
    unittest.main()

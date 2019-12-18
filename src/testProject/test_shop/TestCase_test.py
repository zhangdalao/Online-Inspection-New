# -*- coding=utf-8 -*-
# Author: Yuan Luo
# @Date : 2019-12-16


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
count = 0


@ddt.ddt
class TestCaseTest(RunTest):
    """PC测试环境相关用例"""

    # 获取当前文件路径god
    project = os.path.dirname(__file__)[-4:]
    # 读取xls中god列
    a = ReadData(project, project)
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

    @ddt.data(*a.get_data_by_api(fieldname, "EstateAll"))
    def test_EstateAll(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "EstateMy"))
    def test_EstateMy(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BasicEdit"))
    def test_BasicEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "PropertyEdit"))
    def test_PropertyEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "LayoutEdit"))
    def test_LayoutEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BuildEdit"))
    def test_BuildEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "HouseHoldEdit"))
    def test_HouseHoldEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "AmenityEdit"))
    def test_AmenityEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "DeveloperEdit"))
    def test_DeveloperEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "SalesOffEdit"))
    def test_SalesOffEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectList"))
    def test_ProjectList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectBasEdit"))
    def test_ProjectBasEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectBuildinglist"))
    def test_ProjectBuildinglist(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectLayoutList"))
    def test_ProjectLayoutList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectHouseholdList"))
    def test_ProjectHouseholdList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "SellingEdit"))
    def test_SellingEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "SellingList"))
    def test_SellingList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "AttachmentAdd"))
    def test1_AttachmentAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ProAttachmentList"))
    def test2_ProAttachmentList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)
        sss["attachmentId"] = self.res['data'][0]['attachmentId']

    @ddt.data(*a.get_data_by_api(fieldname, "AttachmentRemove"))
    def test3_AttachmentRemove(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "Links"))
    def test_Links(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "PassiveLinks"))
    def test_PassiveLinks(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BriefEdit"))
    def test_BriefEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BriefDetail"))
    def test_BriefDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketList"))
    def test_MarketList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketDetail"))
    def test_MarketDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketRefruleEdit"))
    def test_MarketRefruleEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketGuideruleEdit"))
    def test_MarketGuideruleEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketSettleruleEdit"))
    def test_MarketSettleruleEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "SiteProjectEdit"))
    def test_SiteProjectEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "Site"))
    def test_Site(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "DynamicAdd"))
    def test1_DynamicAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "DynamicList"))
    def test2_DynamicList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)
        sss["id"] = self.res['data']['pageData'][0]['id']

    @ddt.data(*a.get_data_by_api(fieldname, "DynamicEdit"))
    def test3_DynamicEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "DynamicDel"))
    def test4_DynamicDel(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["id"])+"/del"
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "Operation"))
    def test_Operation(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationEdit"))
    def test_OperationEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "StockEdit"))
    def test_StockEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "Stock"))
    def test_Stock(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BusinessEdit"))
    def test_BusinessEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BusinessAttaAdd"))
    def test1_BusinessAttaAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BusinessAttaList"))
    def test2_BusinessAttaList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # uri = self.a.get_apiPath(self.fieldname, self.apiName)
        # print("uri", len((uri)))
        # url = self.a.get_domains()[env] + uri
        # url = url[0]
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)
        sss["contractId"] = self.res['data']['pageData'][0]['contractId']

    @ddt.data(*a.get_data_by_api(fieldname, "BusinessAttaDel"))
    def test3_BusinessAttaDel(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "LicenseList"))
    def test_LicenseList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "AttachmentList"))
    def test_AttachmentList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "MeterList"))
    def test_MeterList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "UserList"))
    def test_UserList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "TradeList"))
    def test_TradeList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "SettlementList"))
    def test_SettlementList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ThirdMappingList"))
    def test_ThirdMappingList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "BuggetList"))
    def test_BuggetList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "IntercityList"))
    def test_IntercityList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "CouponList"))
    def test_CouponList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "AwardList"))
    def test_AwardList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "PlacementList"))
    def test_PlacementList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 cookies=sss["cookies"], verify=False)
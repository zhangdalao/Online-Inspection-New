# -*- coding=utf-8 -*-
# Author: Yuan Luo
# @Date : 2019-09-21


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
count = 0


@ddt.ddt
class ProjectTest(RunTest):
    """楼盘相关用例"""

    # 获取当前文件路径god
    project = os.path.dirname(__file__)[-4:]
    # 读取xls中god列
    a = ReadData(project,"shop")
    # 通过类名获取模块名
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

    def setUp(self):
        globals()['count'] += 1
        self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))

    def tearDown(self):
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectList"))
    def test_ProjectList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目列表异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectBasEdit"))
    def test_ProjectBasEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目基本信息编辑异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectBuildinglist"))
    def test_ProjectBuildinglist(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目楼栋列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectLayoutList"))
    def test_ProjectLayoutList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目楼栋列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectHouseholdList"))
    def test_ProjectHouseholdList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目楼栋列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "BriefEdit"))
    def test_BriefEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目介绍异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Links"))
    def test_Links(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"关联项目查询异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "AddMarket"))
    def test_AddMarket(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"新增推广方案异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "SiteProjectEdit"))
    # def test_SiteProjectEdit(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
    #     # 调用接口发起请求
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False, timeout=10)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"编辑案场规则异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
    #         raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "DynamicEdit"))
    # def test_DynamicEdit(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
    #     # 调用接口发起请求
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False, timeout=10)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"编辑动态异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
    #         raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "AttachmentAdd"))
    # def test_AttachmentAdd(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
    #     # 调用接口发起请求
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"新增附件异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
    #         raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "ProAttachmentList"))
    # def test_ProAttachmentList(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
    #     # 调用接口发起请求
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False, timeout=10)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"项目资料列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
    #         raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "AttachmentRemove"))
    # def test_AttachmentRemove(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[5:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
    #     # 调用接口发起请求
    #     res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"项目资料移除异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
    #         raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Operation"))
    def test_Operation(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目运营查询异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "OperationEdit"))
    def test_OperationEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目运营编辑异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "StockEdit"))
    def test_StockEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目货量编辑异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "BusinessEdit"))
    def test_BusinessEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目合作方案编辑异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "LicenseList"))
    def test_LicenseList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目评估列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "AttachmentList"))
    def test_AttachmentList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"风险评估列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "MeterList"))
    def test_MeterList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"利润测算表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "UserList"))
    def test_UserList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False, timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"团队管理列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "TradeList"))
    def test_TradeList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"闪佣宝列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "SettlementList"))
    def test_SettlementList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"结算规则列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "ThirdMappingList"))
    def test_ThirdMappingList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"开发商对接列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "BuggetList"))
    def test_BuggetList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目预算列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "BuggetList"))
    def test_BuggetList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        res = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, cookies=sss["cookies"], verify=False)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"项目预算列表异常，接口返回为：{self.res}, 接口预期结果为：{self.expect}")
            raise err

if __name__ == '__main__':
    unittest.main()
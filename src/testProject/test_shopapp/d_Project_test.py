# -*- coding=utf-8 -*-
# Author: Yuan Luo
# @Date : 2019-09-30


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
    """项目相关用例"""

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

    @ddt.data(*a.get_data_by_api(fieldname, "List"))
    def test_List(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "SearchProject"))
    def test_SearchProject(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "Detail"))
    def test_Detail(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "WechatGroup"))
    def test1_WechatGroup(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "Wechat"))
    def test2_Wechat(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)
        sss["wechatGroupId"] = self.res['data'][0]['wechatGroupId']

    @ddt.data(*a.get_data_by_api(fieldname, "WechatEdit"))
    def test3_WechatEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["wechatGroupId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    # @ddt.data(*a.get_data_by_api(fieldname, "WechatRemove"))
    # def test4_WechatRemove(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[6:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["wechatGroupId"])
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
    #                      timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectShare"))
    def test_ProjectShare(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "Projecttemplate"))
    def test_Projecttemplate(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CustomerList"))
    def test_CustomerList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "MarketList"))
    def test_MarketList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "SettlmentList"))
    def test_SettlmentList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "LiveAdd"))
    def test1_LiveAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "LiveList"))
    def test2_LiveList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)
        # sss["roomId"] = res.json()['data']['pageData'][0]['roomId']

    @ddt.data(*a.get_data_by_api(fieldname, "LiveRemove"))
    def test3_LiveRemove(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "VideoAdd"))
    def test1_VideoAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "VideoList"))
    def test2_VideoList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)
        sss["videoId"] = self.res['data'][0]['projectVideo']['videoId']

    @ddt.data(*a.get_data_by_api(fieldname, "VideoDetail"))
    def test3_VideoDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["videoId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "VideoRemove"))
    def test4_VideoRemove(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName) + str(sss["videoId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "HouseConfig"))
    def test1_HouseConfig(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "HousebuildingNos"))
    def test2_HousebuildingNos(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "Household"))
    def test3_Household(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "HouseholdEdit"))
    def test4_HouseholdEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ReceivableTrend"))
    def test_ReceivableTrend(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ReceivableSummary"))
    def test_ReceivableSummary(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "UnreceiptSummary"))
    def test_UnreceiptSummary(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ReceiptSummary"))
    def test_ReceiptSummary(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectMonData"))
    def test_ProjectMonData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectWeekData"))
    def test_ProjectWeekData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectDayData"))
    def test_ProjectDayData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "Data"))
    def test_Data(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationDayData"))
    def test_OperationDayData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationWeekData"))
    def test_OperationWeekData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationMonData"))
    def test_OperationMonData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationMonDataRer"))
    def test_OperationMonDataRer(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationMonDataGuide"))
    def test_OperationMonDataGuide(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationMonDataPurch"))
    def test_OperationMonDataPurch(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperationMonDataBook"))
    def test_OperationMonDataBook(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "FinanceDayData"))
    def test_FinanceDayData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "FinanceWeekData"))
    def test_FinanceWeekData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "FinanceMonData"))
    def test_FinanceMonData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ChannelWeekData"))
    def test_ChannelWeekData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ChannelStoreDetail"))
    def test_ChannelStoreDetail(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectDaySum"))
    def test_ProjectDaySum(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectWeekSum"))
    def test_ProjectWeekSum(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ProjectMonSum"))
    def test_ProjectMonSum(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "DailiesList"))
    def test_DailiesList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "DailyDetail"))
    def test_DailyDetail(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "DailyEdit"))
    def test_DailyEdit(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OperPlanList"))
    def test_OperPlanList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "MarCenter"))
    def test_MarCenter(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardTopData"))
    def test_GuideAwardTopData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardBudget"))
    def test_GuideAwardBudget(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardBudgetSubmit"))
    def test_GuideAwardBudgetSubmit(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardPublish"))
    def test_GuideAwardPublish(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardList"))
    def test_GuideAwardList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardExchange"))
    def test_GuideAwardExchange(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "GuideAwardExcList"))
    def test_GuideAwardExcList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderAwardTopData"))
    def test_OrderAwardTopData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderAwardBudget"))
    def test_OrderAwardBudget(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderAwardList"))
    def test_OrderAwardList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderAwardExchange"))
    def test_OrderAwardExchange(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "OrderAwardExcList"))
    def test_OrderAwardExcList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareAwardTopData"))
    def test_ShareAwardTopData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareBudgetData"))
    def test_ShareBudgetData(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareAwardBudget"))
    def test_ShareAwardBudget(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareAwardList"))
    def test_ShareAwardList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareCouponCode1"))
    def test_ShareCouponCode1(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareCouponCode3"))
    def test_ShareCouponCode3(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareCouponCode4"))
    def test_ShareCouponCode4(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareCouponCode5"))
    def test_ShareCouponCode5(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "ShareSearch"))
    def test_ShareSearch(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CommissionList"))
    def test_CommissionList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "SellingTag"))
    def test_SellingTag(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "SellingAdd"))
    def test_SellingAdd(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "SellingList"))
    def test_SellingList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionTag"))
    def test_QuestionTag(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "CommonQuestionList"))
    def test_CommonQuestionList(self, value):
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
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionAdd"))
    def test1_QuestionAdd(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionList"))
    def test2_QuestionList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)
        sss["questionId"] = self.res['data']['pageData'][0]['questionDto']['questionId']
        sss["answerId"] = self.res['data']['pageData'][0]['answerList'][0]['answerId']

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionBit"))
    def test3_QuestionBit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionEdit"))
    def test4_QuestionEdit(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

    @ddt.data(*a.get_data_by_api(fieldname, "QuestionDelete"))
    def test5_QuestionDelete(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["questionId"])
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调用接口发起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False, timeout=10)

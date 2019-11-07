# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08


import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
import json

count = 0


@ddt.ddt
class commissionTest(RunTest):
    """结佣模块"""

    # 通过文件名夹获取project参数的值
    project = os.path.dirname(__file__)[-4:]
    # 读取文件实例化
    a = ReadData(project, project)
    # 通过类名获取fieldname的值
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
        with open('commission.txt', 'r', encoding='utf-8') as f:
            lines = list(f)
            cookie = lines[0].strip('\n')
        cls.cookies = cookie
        sss["timestamp"] = cls.timestamp
        sss["cookie"] = cls.cookies

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
                raise err
        elif self.result and type(self.result) == str:
            send_ding(self.robot_url, self.mobile, content=f"{self.desc}测试失败！\n测试反馈:{self.result}")
            raise Exception
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "commissionReport"))
    def test_commissionReport(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionorg"))
    def test_commissionorg(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionDetail"))
    def test_commissionDetail(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionorderList"))
    def test_commissionorderList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
        sss["orderId"] = int(sss["orderId"])

    @ddt.data(*a.get_data_by_api(fieldname, "commission_agreementList"))
    def test_commission_agreementList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commission_agreement"))
    def test_commission_agreement(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commission_givebackCarrier"))
    def test_commission_givebackCarrier(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionorderlnfo"))
    def test_commissionorderlnfo(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionList"))
    def test_commissionList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionStoreList"))
    def test_commissionStoreList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionBranch"))
    def test_commissionBranch(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionDeal"))
    def test_1commissionDeal(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[6:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionAccountList"))
    def test_commissionAccountList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionApply"))
    def test_commissionApply(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionInfo"))
    def test_commissionInfo(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

    @ddt.data(*a.get_data_by_api(fieldname, "commissionCancel"))
    def test_commissionCancel(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)

if __name__ == '__main__':
    unittest.main()
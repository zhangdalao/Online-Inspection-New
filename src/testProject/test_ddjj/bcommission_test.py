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
import requests
import urllib3

count = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@ddt.ddt
class commissionTest(RunTest):
    """佣金模块"""

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
                self.logger.error("测试结果         :测试失败！")
                send_ding(self.robot_url, self.mobile,
                          content=f"{self.desc}测试失败！\n接口返回为：{self.res}, 预期结果为：{self.expect}")
                raise err
        elif self.result and type(self.result) == str:
            send_ding(self.robot_url, self.mobile, content=f"{self.desc}测试失败！\n测试反馈:{self.result}")
            raise Exception
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "aCommissionStatistic"))
    def test_aCommissionStatistic(self, value):
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
        sss["cookies"] = ";".join(['{}={}'.format(*_) for _ in sss["cookie"].items()])
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "bcommissionorg"))
    def test_bcommissionorg(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "cCommissionList"))
    def test_cCommissionList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "dCommissionFactoringInfo"))
    def test_dCommissionFactoringInfo(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "exfProtocolList"))
    def test_exfProtocolList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "fxfProtocolInfo"))
    def test_fxfProtocolInfo(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "gReferralList"))
    def test_gReferralList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "hGuideList"))
    def test_hGuideList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "iOrderList"))
    def test_iOrderList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "kOperator"))
    def test_kOperator(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "lProjectList"))
    def test_lProjectList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "mApplyProtocolUrl"))
    def test_mApplyProtocolUrl(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "nSettlementList"))
    def test_nSettlementList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "oBankAcountList"))
    def test_oBankAcountList(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "paddFastSettlement"))
    def test_paddFastSettlement(self, value):
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
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "qFactoringCancel"))
    def test_qFactoringCancel(self, value):
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
        sss["hash_commissionApplyId"] = '{"commissionApplyType":2,"commissionApplyId":"' + sss["hash_commissionApplyId"] + '"}'
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                            self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)


if __name__ == '__main__':
    unittest.main()
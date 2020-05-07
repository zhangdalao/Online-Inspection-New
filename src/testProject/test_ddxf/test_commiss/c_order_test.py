__author__ = 'fdd'
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
import requests
import time

count = 0

@ddt.ddt
class OrderTest(RunTest):
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
        cls.result = None
        cls.desc = None

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

    @ddt.data(*a.get_data_by_api(fieldname, "ByPassword"))
    def test_ByPassword(self, value):
        self.desc = value[self.desc_num]
        sss["version"] = sss["versionName"][1:]
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        # print(sss["versionName"])
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["commiss"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num , self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, verify=False)
        sss["userId"] = str(sss["userId"])

    @ddt.data(*a.get_data_by_api(fieldname, "cOrder"))
    def test_cOrder(self, value):
        self.desc = value[self.desc_num]
        self.apiName = (inspect.stack()[0][3])[5:]
        env = value[self.env_num]

        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["commiss"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [str(sss["userId"]), str(sss["token"]), self.timestamp, value[self.method_num].upper(), uri]
        # print("签名",str_sign_list)
        value.append(str_sign_list)
        print("签名", value)
        sss["version"] = sss["versionName"][1:]
        # # # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value)
        time.sleep(3)

    @ddt.data(*a.get_data_by_api(fieldname, "dOrderSign"))
    def test_dOrderSign(self, value):
        self.desc = value[self.desc_num]
        self.apiName = (inspect.stack()[0][3])[5:]  # 表示读取列表中的第一个元素（字典元素)的第三个元素？？？？？但是第三个应该是 请求头啊
        env = value[self.env_num]
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["commiss"][env] + uri  # a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        str_sign_list = [str(sss["userId"]), str(sss["token"]), self.timestamp, value[self.method_num].upper(), uri]
        # print(str_sign_list)
        value.append(str_sign_list)
        # print(value)
        sss["version"] = sss["versionName"][1:]
        # # # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value)

    @ddt.data(*a.get_data_by_api(fieldname, "dOrderSign1"))
    def test_dOrderSign1(self, value):
        self.desc = value[self.desc_num]
        self.apiName = (inspect.stack()[0][3])[5:]  # 表示读取列表中的第一个元素（字典元素)的第三个元素？？？？？但是第三个应该是 请求头啊
        env = value[self.env_num]
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["commiss"][env] + uri  # a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        str_sign_list = [str(sss["userId"]), str(sss["token"]), self.timestamp, value[self.method_num].upper(), uri]
        # print(str_sign_list)
        value.append(str_sign_list)
        # print(value)
        sss["version"] = sss["versionName"][1:]
        # # # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value)


    @ddt.data(*a.get_data_by_api(fieldname, "eaddconfirm"))
    def test_eaddconfirm(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "fconfirm"))
    def test_fconfirm(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)
        time.sleep(2)
    @ddt.data(*a.get_data_by_api(fieldname, "gticket"))
    def test_gticket(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "gticketdetail"))
    def test_gticketdetail(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "hvioce"))
    def test_hvioce(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "ivioceconfirm"))
    def test_ivioceconfirm(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "jmoney"))
    def test_jmoney(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "kmoneyconfirm"))
    def test_kmoneyconfirm(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "lconfirmlist"))
    def test_lconfirmlist(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "mconfirmget"))
    def test_mconfirmget(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)
    time.sleep(5)

    @ddt.data(*a.get_data_by_api(fieldname, "mdcheckcommiss"))
    def test_mdcheckcommiss(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "napplylist"))
    def test_napplylist(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "nfactoring"))
    def test_nfactoring(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

        time.sleep(8)

    @ddt.data(*a.get_data_by_api(fieldname, "ofactoringamuont"))
    def test_ofactoringamuont(self, value):
        self.desc = value[self.desc_num]
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数

        env = value[self.env_num]
        # 通过环境参数获得接口url
        url = self.a.get_domains()["commiss"][env] + self.a.get_apiPath(self.fieldname, self.apiName)
        # 调用接口发起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num,
                                 value, cookies=sss["cookies"], verify=False)

        print("关联的数据等于", sss)









if __name__ == '__main__':
    unittest.main()










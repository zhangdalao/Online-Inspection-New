__author__ = 'fdd'
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
import requests
import urllib3
import random

count = 0

@ddt.ddt
class ddmfTest(RunTest):
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

    @ddt.data(*a.get_data_by_api(fieldname, "aaloginddmf"))
    def test_aaloginddmf(self, value):

        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)
        sss["cookies1"] = requests.utils.dict_from_cookiejar(self.result.cookies)
        sss['userIdd'] = str(sss['userIdd'])

        print(sss)




    @ddt.data(*a.get_data_by_api(fieldname, "nSettlementList"))
    def test_nSettlementList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        dict_cookie = sss["cookies1"]
        sss["cookies2"] = ";".join(['{}={}'.format(*_) for _ in dict_cookie.items()])
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)
        #请求响应的data返回结果
        data_list = sss["dataresult"]
        print(data_list)
        data_dict = {}
        key = sss["orderNumber"]
        value = sss["commissionId"]
        for i in range(0,len(key)):
            data_dict[key[i]] = value[i]
        print("返回的列表为",data_dict)
        orderId = sss["orderId"]
        print (orderId)
        sss["commissionIdreal"] = data_dict[str(orderId)]
        print (sss["commissionIdreal"])

        #请求响应的orderId，全部提取出来，放到一个列表里
        # order_list = sss["orderNumber"]
        # print(order_list)
        # #遍历要请佣的orderId在order_list的位置，并且将下标返回
        # orderIdtest = str(sss["orderId"])
        # print(orderIdtest)
        # print (len(order_list))
        # for i in range(1,len(order_list)):
        #     if order_list[i] == orderIdtest:
        #         #在dataresult这个列表里，把这个下表元素提取出来,这个元素是一个字
        #         sss["index"] = i
        #         #然后再把这个字典中的factoringCommissionId取出来，作为请佣时传入的factoringCommissionId
        #     else:
        #         print ("列表里没有这个order")
        # print (sss["index"])
        # index = sss["index"]
        # data_dict = data_list[index]
        # #sss["factoringCommissionId"] = data_dict["factoringCommissionId"]






    @ddt.data(*a.get_data_by_api(fieldname, "oBankAcountList"))
    def test_oBankAcountList(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "paddFastSettlement"))
    def test_paddFastSettlement(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "pbgetthebussinessId"))
    def test_pbgetthebussinessId(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "qupload"))
    def test_qupload(self, value):
        # 通过函数名获取apiName参数的值
        self.apiName = (inspect.stack()[0][3])[5:]
        # 获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()["ddmf"][env] + uri
        sss["invoiceCode"] = random.randint(12345678,87654321)
        sss["invoiceNo"] = random.randint(12345678,98765432)
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        str_sign_list = [self.timestamp, value[self.method_num].upper(), uri]
        value.append(str_sign_list)
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num,
                                 self.headers_num, self.para_num,
                                 self.data_num, self.desc_num, self.relateData_num, self.expect_num, value,
                                 verify=False)

        time.sleep(5)




if __name__ == '__main__':
    unittest.main()
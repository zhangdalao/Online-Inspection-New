__author__ = 'fdd'
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding
import time

count = 0

@ddt.ddt
class ExpansionListTest(RunTest):
    project = os.path.dirname(__file__)[-4:]
    a = ReadData(project, project)
    fieldname = sys._getframe().f_code.co_name[:-4]
    # 获取项目名后，获取机器人相关配置
    json_dict = a.json_data[project]["robot_data"]
    robot_url = json_dict["robot_url"]
    mobile = json_dict["mobile"]
    #线上楼盘ID
    sss["Restful_estateId2"] = json.dumps({"estateId":"1041394"})
    sss["Restful_estateId3"] = json.dumps({"estateId": "22374"})
    #查看线上签约信息
    sss["Restful_signId"] = json.dumps({"estateId": "22374", "signId": "32"})
    #查看测试环境签约信息
    sss["Restful_signId_test"] = json.dumps({"estateId": "889", "signId": "66"})

    # 读取签约结束日期时间戳
    sep = os.sep
    root_path = os.path.abspath(os.path.join(__file__, f"..{sep}"))
    filePath = f"{root_path}{sep}remark.txt"
    with open(filePath, 'r') as f:
        sign_end_time = f.read()  # 读取签约结束时间戳
    sss["sign_end_time"]= int(sign_end_time)
    # 写入新的签约时间戳，以备下次使用
    with open(filePath, 'r+') as f:  # 打开文件
        new_end_time = int(sign_end_time) + 86400000
        f.write(str(new_end_time))

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
                self.logger.error("测试结果         :测试失败！")
                send_ding(self.robot_url, self.mobile,
                          content=f"{self.desc}测试失败！\n接口返回为：{self.res}, 预期结果为：{self.expect}")
                raise err
        elif self.result and type(self.result) == str:
            send_ding(self.robot_url, self.mobile, content=f"{self.desc}测试失败！\n测试反馈:{self.result}")
            raise Exception
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "get_expansionlist"))
    def test_get_expansionlist(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "add_expansion"))
    def test_add_expansion(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "add_signinfo"))
    def test_add_signinfo(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)
        sss["signId"] = str(sss["signId"])
        sss["Restful_new_signId"] = json.dumps({"estateId": 22374, "signId": sss["signId"]})
        sss["Restful_new_signId_test"] = json.dumps({"estateId": 890, "signId": sss["signId"]})

    @ddt.data(*a.get_data_by_api(fieldname, "add_signinfo_failed"))
    def test_add_signinfo_failed(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "get_signinfo"))
    def test_get_signinfo(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "update_signinfo"))
    def test_update_signinfo(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)
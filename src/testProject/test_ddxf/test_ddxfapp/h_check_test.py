__author__ = 'fdd '
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
class CheckTest(RunTest):
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

    @ddt.data(*a.get_data_by_api(fieldname, "arefund"))
    def test_arefund(self, value):
        self.desc = value[self.desc_num]
        self.apiName = (inspect.stack()[0][3])[5:]
        env = value[self.env_num]

        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
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

    @ddt.data(*a.get_data_by_api(fieldname, "auditchange"))
    def test_auditchange(self, value):
        self.desc = value[self.desc_num]
        self.apiName = (inspect.stack()[0][3])[5:]
        env = value[self.env_num]

        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri
        str_sign_list = [str(sss["userId"]),str(sss["token"]),self.timestamp, value[self.method_num].upper(), uri]
        # print(str_sign_list)
        value.append(str_sign_list)
        # print(value)
        sss["version"] = sss["versionName"][1:]
        # # # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num,
                                 self.para_num, self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
        time.sleep(5)






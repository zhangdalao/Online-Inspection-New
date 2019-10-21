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

    @ddt.data(*a.get_data_by_api(fieldname, "auditchange"))
    def test_auditchange(self, value):
        self.apiName = (inspect.stack()[0][3])[5:]  #表示读取列表中的第一个元素（字典元素)的第三个元素？？？？？但是第三个应该是 请求头啊
        env = value[self.env_num]

        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #a.get_domains是字典，因为有好几个环境，根据测试环境来获得域名，域名+uri就是访问地址
        # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
        print(sss)
        print(sss["userId"])
        print(sss["token"])
        str_sign_list = [str(sss["userId"]),str(sss["token"]),self.timestamp, value[self.method_num].upper(), uri]
        print(str_sign_list)
        value.append(str_sign_list)
        print(value)
        sss["version"] = sss["versionName"][1:]
        # # # 调起请求
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value)
        time.sleep(5)
        # #
        # #
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"审核失败！！！接口返回为：{err}, 接口预期结果为：{self.expect}")
            raise err






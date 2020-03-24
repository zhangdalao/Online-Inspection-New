__author__ = 'fdd'
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import *
from src.common.dingDing import send_ding

count = 0

@ddt.ddt
class PackageTest(RunTest):
    project = os.path.dirname(__file__)[-4:]
    a = ReadData(project, project)
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
        ##线上货包ID，项目ID
        sss["restful_packageId"]=json.dumps({"packageId": "9"})
        sss["restful_packageEstateId"] = json.dumps({"packageEstateId": "21"})
        ##预发布货包ID，项目ID
        sss["restful_packageId_pre"] = json.dumps({"packageId": "8"})
        sss["restful_packageEstateId_pre"] = json.dumps({"packageEstateId": "19"})
        ##测试环境货包ID，项目ID
        sss["restful_packageId_test"] = json.dumps({"packageId": "135"})
        sss["restful_packageEstateId_test"] = json.dumps({"packageEstateId": "231"})
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

    @ddt.data(*a.get_data_by_api(fieldname, "package_list"))
    def test_01package_list(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "packageEstates_list"))
    def test_02packageEstates_list(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "getPackagesCities"))
    def test_03getPackagesCities(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "packageEstatesDetail"))
    def test_04packageEstatesDetail(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "getPackagesFollows"))
    def test_05getPackagesFollows(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "addAdvice"))
    def test_06addAdvice(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "getCityMarketUsers"))
    def test_07getCityMarketUsers(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "allotFollowUser")) ##指定跟进人
    def test_08allotFollowUser(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "addProgress")) ##添加合作进度
    def test_09addProgress(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

    @ddt.data(*a.get_data_by_api(fieldname, "getSurveyInfo")) ##查看项目调研表
    def test_10getSurveyInfo(self, value):
        self.apiName = (inspect.stack()[0][3])[7:]
        #  获取测试环境参数
        env = value[self.env_num]
        # 通过环境参数获得接口url
        uri = self.a.get_apiPath(self.fieldname, self.apiName)
        url = self.a.get_domains()[env] + uri   #根据环境获取域名拼装url
        # 调起请求
        self.result = self.start(self.project, self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False)

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
class DynamicTest(RunTest):
    """动态相关用例"""

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
        self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))

    @ddt.data(*a.get_data_by_api(fieldname, "Add"))
    def test1_Add(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"新增动态异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "List"))
    def test2_List(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False, timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
            sss["id"] = res.json()['data']['pageData'][0]['id']
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态列表异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Edit"))
    def test3_Edit(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"编辑动态异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Zan"))
    def test4_Zan(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态点赞异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Comment"))
    def test5_Comment(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态评论异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    # @ddt.data(*a.get_data_by_api(fieldname, "Delete"))
    # def test6_Delete(self, value):
    #     # 通过函数名获取apiName参数的值
    #     self.apiName = (inspect.stack()[0][3])[6:]
    #     # 获取测试环境参数
    #     env = value[self.env_num]
    #     # 通过环境参数获得接口url
    #     uri = self.a.get_apiPath(self.fieldname, self.apiName)+str(sss["id"])+"/del"
    #     url = self.a.get_domains()[env] + uri
    #     # ***需要加密的数据在此处添加到列表中即可，反之则不用写这一步***
    #     str_sign_list = [str(sss["userId"]), sss["token"], self.timestamp, value[self.method_num].upper(), uri]
    #     value.append(str_sign_list)
    #     # 调用接口发起请求
    #     print(self.headers_num)
    #     res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
    #                      self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
    #                      timeout=10)
    #     try:
    #         self.assertEqual(True, checkOut(self.res, self.expect))
    #         self.logger.info("测试结果         :测试通过！")
    #     except Exception as err:
    #         self.logger.error("测试结果         :测试失败！")
    #         json_dict = self.a.json_data[self.project]["robot_data"]
    #         robot_url = json_dict["robot_url"]
    #         mobile = json_dict["mobile"]
    #         send_ding(robot_url, mobile, content=f"删除动态异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
    #         raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Share"))
    def test7_Share(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态分享异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "Detail"))
    def test8_Detail(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态详情异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err

    @ddt.data(*a.get_data_by_api(fieldname, "UserInfo"))
    def test9_UserInfo(self, value):
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
        print(self.headers_num)
        res = self.start(self.isSkip_num, self.apiName_num, url, self.method_num, self.headers_num, self.para_num,
                         self.data_num, self.desc_num, self.relateData_num, self.expect_num, value, verify=False,
                         timeout=10)
        try:
            self.assertEqual(True, checkOut(self.res, self.expect))
            self.logger.info("测试结果         :测试通过！")
        except Exception as err:
            self.logger.error("测试结果         :测试失败！")
            json_dict = self.a.json_data[self.project]["robot_data"]
            robot_url = json_dict["robot_url"]
            mobile = json_dict["mobile"]
            send_ding(robot_url, mobile, content=f"动态详情查看经纪人信息异常，接口返回为：{res}, 接口预期结果为：{self.expect}")
            raise err


if __name__ == '__main__':
    unittest.main()
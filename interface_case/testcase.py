__author__ = 'wuxj06'
import unittest
import requests
import ddt
import os

# import user_management_pb2
# import user_management_pb2_grpc
# import register_login_pb2
# import register_login_pb2_grpc
# import comp_management_pb2
# import comp_management_pb2_grpc

import random
import hmac
import time
from BeautifulReport import BeautifulReport
from hashlib import sha256


@ddt.ddt
class interface_case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # filenames = ["access_token.proto",'account.proto','developer.proto','developer_config.proto','dictionary.proto','framework.proto','my_supplier.proto',"project.proto"]
        # for flie in filenames:
        #     os.popen("python -m grpc_tools.protoc -I=D:\Python\\api-common-protos --python_out=D:\Python --grpc_python_out=D:\Python -I=D:\developer_center\micro-developer-service-proto\micro_developer %s"%flie)
        cls.params = {
            "mobile": "15988888888",
            "password": "kfs123456"
        }
        cls.url = "https://m.b2bmir.com/api/user/login/login-by-password"
        cls.response = requests.post(url=cls.url, json=cls.params)
        cls.dict1 = dict(cls.response.json())
        cls.data = cls.dict1["data"]
        cls.headers = {
            "auth-token": cls.data["auth-token"]
        }

        # print(cls.headers)
        list1 = list(range(10))
        a = '10' + str(random.choice(list1))
        b = ''.join(random.choice('0123456789') for j in range(8))
        cls.phone = a + b
        format = "%Y-%m-%d %H:%M:%S"
        t = time.strftime(format, time.localtime())
        timeArray = time.strptime(t, format)
        timeStamp = str(int(time.mktime(timeArray)))
        # timeStamp = '1597231871'
        app_id = 'micro-supplier-service'
        app_key = '3F9Espv8lrcZ2iDA4MqJhTy6QXUzoYax'
        auth = app_id + '&' + timeStamp + '&' + app_key
        md5x = hmac.new(
            bytes(
                app_key,
                encoding='utf-8'),
            bytes(
                auth,
                encoding='utf-8'),
            digestmod=sha256)
        key = md5x.hexdigest()
        cls.channel = grpc.insecure_channel('47.101.38.159:56249')
        cls.metadata1 = (
            ('authorization',
             'bearer %s.{"app_id":"%s","time_stamp":%s}' %
             (key,
              app_id,
              timeStamp)),
        )

    @ddt.file_data("../caseparams_yaml/kfsapi.yaml")
    @ddt.unpack
    def test_case(cls, params, methods, link, case_name):
        cls.__dict__['_testMethodDoc'] = "{}".format(case_name)
        cls.params = params
        cls.response = requests.request(methods,
                                        link,
                                        data=cls.params,
                                        headers=cls.headers)
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", params, '\n', "接口链接：", link)
        cls.assertEqual(
            cls.dict1["success"] or cls.dict1["isok"],
            True,
            msg=case_name + "接口错误")

    # @ddt.file_data("user_management.yaml")
    # @ddt.unpack
    # def test_user_management(cls, case_name, method_name, argument,kwargs):
    #     # cls.__dict__['_testMethodDoc'] = "{}".format(case_name)
    #     cls.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         cls.channel)
    #     cls.response = getattr(cls.stub, method_name)(request=getattr(user_management_pb2,argument)(**kwargs),
    #                                                     metadata=cls.metadata1)
    #     cls.assertIsNotNone(cls.response, msg=case_name + "接口错误")
    #
    # @ddt.file_data("comp_management.yaml")
    # @ddt.unpack
    # def test_comp_management(cls, case_name, method_name, argument, kwargs):
    #     # cls.__dict__['_testMethodDoc'] = "{}".format(case_name)
    #     cls.stub = comp_management_pb2_grpc.CompManagementServiceStub(
    #         cls.channel)
    #     cls.response = getattr(cls.stub, method_name)(request=getattr(comp_management_pb2, argument)(**kwargs),
    #                                                     metadata=cls.metadata1)
    #     cls.assertIsNotNone(cls.response, msg=case_name + "接口错误")
    #
    # @ddt.file_data("register_login.yaml")
    # @ddt.unpack
    # def test_comp_management(cls, case_name, method_name, argument, kwargs):
    #     # cls.__dict__['_testMethodDoc'] = "{}".format(case_name)
    #     cls.stub = register_login_pb2_grpc. RegisterLoginServiceStub(
    #         cls.channel)
    #     cls.response = getattr(cls.stub, method_name)(request=getattr(register_login_pb2, argument)(**kwargs),
    #                                                     metadata=cls.metadata1)
    #     cls.assertIsNotNone(cls.response, msg=case_name + "接口错误")


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(interface_case))
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # 实例化BeautifulReport模块
    run.report(filename='测试报告', description='参数化测试报告')

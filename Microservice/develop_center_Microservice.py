__author__ = 'wuxj06'
import developer_pb2
import developer_pb2_grpc
import developer_config_pb2
import developer_config_pb2_grpc
import grpc
import random
import hmac
import time
import unittest
from BeautifulReport import BeautifulReport
from hashlib import sha256


class Microservice_develop_center(unittest.TestCase):

    def setUp(cls):
        cls.list1 = list(range(10))
        cls.a = '10' + str(random.choice(cls.list1))
        cls.b = ''.join(random.choice('0123456789') for j in range(8))
        cls.phone = cls.a + cls.b
        cls.format = "%Y-%m-%d %H:%M:%S"
        cls.t = time.strftime(cls.format, time.localtime())
        cls.timeArray = time.strptime(cls.t, cls.format)
        cls.timeStamp = str(int(time.mktime(cls.timeArray)))
        # timeStamp = '1597231871'
        cls.app_id = 'appid'
        cls.app_key = 'appkey'
        cls.address = 'address'
        cls.auth = cls.app_id + '&' + cls.timeStamp + '&' + cls.app_key
        cls.md5x = hmac.new(
            bytes(
                cls.app_key,
                encoding='utf-8'),
            bytes(
                cls.auth,
                encoding='utf-8'),
            digestmod=sha256)
        cls.key = cls.md5x.hexdigest()
        cls.channel = grpc.insecure_channel(cls.address)
        cls.metadata1 = (
            ('authorization',
             'bearer %s.{"app_id":"%s","time_stamp":%s}' %
             (cls.key,
              cls.app_id,
              cls.timeStamp)),
        )

    def test_case0001(cls):
        '''通过开发商ID获取开发商信息'''

        cls.stub = developer_pb2_grpc.DeveloperServiceStub(cls.channel)
        cls.response = cls.stub.GetDeveloper(
            developer_pb2.GetDeveloperInfoRequest(developer_id="K006489"
                                                  ), metadata=cls.metadata1)
        print(cls.response)

        cls.assertIsNotNone(cls.response, "过开发商ID获取开发商信息表接口错误")

    def test_case0002(cls):
        '''通过区域code获取开发商列表'''

        cls.stub = developer_pb2_grpc.DeveloperServiceStub(cls.channel)
        cls.response = cls.stub.GetDeveloperByArea(
            developer_pb2.GetDeveloperByAreaRequest(province_code="222",
                                                    city_code="224",
                                                    page=1,

                                                    ), metadata=cls.metadata1)
        print(cls.response)
        cls.assertIsNotNone(cls.response, "通过区域code获取开发商列表接口错误")

    def test_case0003(cls):
        '''通过id批量获取开发商信息(简版)'''


        cls.stub = developer_pb2_grpc.DeveloperServiceStub(cls.channel)
        cls.response = cls.stub.GetDeveloperSimpleInfoList(
            developer_pb2.GetDeveloperSimpleInfoListRequest(developer_id_list=["K000001","K007823"]

                                                    ), metadata=cls.metadata1)
        print(cls.response)

        cls.assertIsNotNone(cls.response, "通过区域code获取开发商列表接口错误")

    def test_case0004(cls):
        '''获取配置信息'''

        cls.stub = developer_config_pb2_grpc.DeveloperConfigServiceStub(cls.channel)
        cls.response = cls.stub.GetDeveloperConfig(
            developer_config_pb2.GetDeveloperConfigRequest(


                                                    ), metadata=cls.metadata1)
        print(cls.response)

        cls.assertIsNotNone(cls.response, "获取配置信息接口错误")

    def test_case0005(cls):
        '''保存开发商信息'''

        cls.stub = developer_pb2_grpc.DeveloperServiceStub(cls.channel)
        cls.response = cls.stub.SaveDeveloper(
            developer_pb2.SaveDeveloperRequest(developer={"developer_id":"K000001",
                                                          "reg_address":"cesiceshi"


            }), metadata=cls.metadata1)
        print(cls.response)

        cls.assertIsNotNone(cls.response, "通过区域code获取开发商列表接口错误")


if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(Microservice_develop_center))
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # 实例化BeautifulReport模块
    run.report(filename='开发商中心微服务接口测试报告', description='开发商中心微服务接口')


__author__ = 'wuxj06'
# import developer_pb2
# import developer_pb2_grpc
# import developer_config_pb2
# import developer_config_pb2_grpc
import grpc
import random
import hmac
import time
from hashlib import sha256
import sys
import unittest
from BeautifulReport import BeautifulReport
# from beidou.caserunfile.Microservice import develop_center_Microservice
sys.path.append("/root/.jenkins/jobs/beidou_interfacecase/workspace/")
from beidou.caserunfile.interface_case import testcase
from beidou.caserunfile.interface_case import other_testcase

class Test(unittest.TestCase):
    {}


if __name__ == '__main__':
    # 执行测试
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(
        loader.loadTestsFromTestCase(
            testcase.interface_case))
    test_suite.addTests(
        loader.loadTestsFromTestCase(
            other_testcase.OtherCase))
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # 实例化BeautifulReport模块

    run.report(filename='beiDouInterface_testReport', description='北斗组接口测试用例')

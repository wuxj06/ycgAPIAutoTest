__author__ = 'wuxj06'
import message_sms_pb2
import message_sms_pb2_grpc
import message_pb2
import message_pb2_grpc
import message_partner_config_pb2
import message_partner_config_pb2_grpc
import user_management_pb2
import user_management_pb2_grpc
import grpc
import os
import random
import hmac
import time
import unittest
from BeautifulReport import BeautifulReport
from hashlib import sha256


class msn_center(unittest.TestCase):

    def setUp(self):
        filenames = ["access_token.proto",'message.proto','message_name_config.proto','message_partner_config.proto','message_queue.proto','message_sms.proto','message_template.proto']
        for flie in filenames:
            os.popen("python -m grpc_tools.protoc -I=D:\Python\python-api-common-protos-master --python_out=D:\Python --grpc_python_out=D:\Python -I=D:\\message_center\msn-service-center-proto\msn %s"%flie)
        # self.list1 = list(range(10))
        # self.a = '10' + str(random.choice(self.list1))
        # self.b = ''.join(random.choice('0123456789') for j in range(8))
        # self.phone = self.a + self.b
        self.format = "%Y-%m-%d %H:%M:%S"
        self.t = time.strftime(self.format, time.localtime())
        self.timeArray = time.strptime(self.t, self.format)
        self.timeStamp = str(int(time.mktime(self.timeArray)))
        # timeStamp = '1597231871'
        self.app_id = "appid"
        self.app_key = 'appkey'
        self.auth = self.app_id + '&' + self.timeStamp + '&' + self.app_key
        self.md5x = hmac.new(
            bytes(
                self.app_key,
                encoding='utf-8'),
            bytes(
                self.auth,
                encoding='utf-8'),
            digestmod=sha256)
        self.key = self.md5x.hexdigest()
        self.channel = grpc.insecure_channel('address')
        self.metadata1 = (
            ('authorization',
             'bearer %s.{"app_id":"%s","time_stamp":%s}' %
             (self.key,
              self.app_id,
              self.timeStamp)),
        )

        # print(self.metadata1)

    # def test_case0001(self):
    #     '''??????????????????,???????????????'''
    #
    #     self.stub = message_sms_pb2_grpc.SendServiceStub(
    #         self.channel)
    #     self.response = self.stub.SendSms(
    #         message_sms_pb2.SendSmsRequest(
    #             biz_code="common_sns",
    #             type=2,
    #             send_Type=2,
    #             phone="13077847823",
    #             temp_key="aicard-interact-app-push",
    #             temp_params="visit_user_name=1&share_user_name=2&action_string=3",
    #             sms_content=""
    #
    #         ), metadata=self.metadata1
    #     )
        # print(self.response)
        # print(self.metadata1)
        # self.assertIsNotNone(self.response, "??????????????????,???????????????????????????")

    # def test_case0002(self):
    #     '''????????????????????????????????????'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.SendVerifyCode(
    #         user_management_pb2.SendVerifyCodeReq(
    #             phone="13024082335"
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "????????????????????????????????????????????????")

    # def test_case0003(self):
    #     '''????????????'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.ChangePassword(
    #         user_management_pb2.ChangePasswordReq(
    #             user_id="100001",
    #             captcha="433488",
    #             new_password="kfs123456"
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "????????????????????????")

    # def test_case0004(self):
    #     '''?????????????????????'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.ChangePhone(
    #         user_management_pb2.ChangePhoneReq(
    #             user_id="100001",
    #             captcha="433488",
    #             phone="13760489226"
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "?????????????????????????????????")
    # def test_case0005(self):
    #     '''???????????????????????????????????????'''
    #
    #     self.stub = message_pb2_grpc.MessageServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetMessageList(
    #         message_pb2.GetMessageListRequest(
    #             page={"page_size":10,"current_page":1,"total":10},
    #             condition={"user_id":"173663","keyword":"","type":0,"datatype":1}
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "???????????????????????????????????????????????????")
    #
    # def test_case0006(self):
    #     '''??????????????????????????????'''
    #
    #     self.stub = message_pb2_grpc.MessageServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUnreadMessageCount(
    #         message_pb2.GetMessageRequest(
    #
    #             user_id="198311"
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "??????????????????????????????????????????")
    #
    # def test_case0007(self):
    #     '''????????????????????????'''
    #     self.stub = message_partner_config_pb2_grpc.MessagePartnerConfigServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetMessagePartnerConfigList(
    #         message_partner_config_pb2.GetMessagePartnerConfigListRequest(
    #
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "????????????????????????????????????")




if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(msn_center))
    # # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # ?????????BeautifulReport??????
    run.report(filename='???????????????????????????????????????', description='???????????????????????????')
    unittest.main()
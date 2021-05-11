__author__ = 'wuxj06'
import user_management_pb2
import user_management_pb2_grpc
import register_login_pb2
import register_login_pb2_grpc
import comp_management_pb2
import comp_management_pb2_grpc
import company_cert_pb2
import company_cert_pb2_grpc
import grpc
import random
import hmac
import time
import unittest
import yaml
from BeautifulReport import BeautifulReport
from hashlib import sha256

class user_center(unittest.TestCase):

    def setUp(self):
        self.list1 = list(range(10))
        self.a = '10' + str(random.choice(self.list1))
        self.b = ''.join(random.choice('0123456789') for j in range(8))
        self.phone = self.a+self.b
        self.format = "%Y-%m-%d %H:%M:%S"
        self.t = time.strftime(self.format,time.localtime())
        self.timeArray = time.strptime(self.t, self.format)
        self.timeStamp = str(int(time.mktime(self.timeArray)))
        # timeStamp = '1597231871'
        self.app_id = 'appid'
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
            ('authorization', 'bearer %s.{"app_id":"%s","time_stamp":%s}' % (self.key,self.app_id, self.timeStamp)),)



# def run():
    # format = "%Y-%m-%d %H:%M:%S"
    # t = time.strftime(format, time.localtime())
    # timeArray = time.strptime(t, format)
    # timeStamp = str(int(time.mktime(timeArray)))
    # #timeStamp = '1597231871'
    # app_id = 'micro-supplier-service'
    # app_key = '748e4880546c5004d0164d70ce8df743'
    # auth = app_id + '&' + timeStamp + '&' + app_key
    # md5x = hmac.new(
    #     bytes(
    #         app_key,
    #         encoding='utf-8'),
    #     bytes(
    #         auth,
    #         encoding='utf-8'),
    #     digestmod=sha256)
    # key = md5x.hexdigest()
    # channel = grpc.insecure_channel('47.101.38.159:31009')
    # metadata1 = (
    #     ('authorization', 'bearer %s.{"app_id":"micro-supplier-service","time_stamp":%s}' %(key, timeStamp)), )
    #
    # stub = user_management_pb2_grpc.UserManagementServiceStub(channel)
    # response = stub.GetUserInfoListByCompanyId(
    # user_management_pb2.GetUserInfoListByCompanyIdReq(company_id="G151485",page=1,page_size=10
    #                                                  ),metadata=metadata1)
    # response2 = stub.AddCompanyInfo(
    #     user_management_pb2.AddCompanyInfoReq(
    #                     company_id="G104411",
    #                     company_name= "深圳市冰融科技有限司",
    #                     company_type=1,
    #                     company_logo= "adafaafagg",
    #                     source= 1,
    #                     status=1,
    #                     created_by="阿的江"
    #     ),metadata=metadata1
    # )
    # print(auth)
    # print(key)
    # # dict1 = dict(response2)
    # print("Greeter client received: " + str(response),str(response1),response2.success)
    # def test_case0001(self):
    #     '''通过公司ID获取用户信息列表'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(self.channel)
    #     self.response = self.stub.GetUserInfoListByCompanyId(
    #     user_management_pb2.GetUserInfoListByCompanyIdReq(company_id="K006395",page=1,page_size=10,search={"name":"王"}
    #                                                 ),metadata=self.metadata1)
    #     # print(self.response)
    #     self.assertIsNotNone(self.response,  "通过公司ID获取用户信息列表接口错误")
    #
    # def test_case0002(self):
    #     '''编辑用户信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(self.channel)
    #     self.response = self.stub.SaveUserInfo(
    #     user_management_pb2.SaveUserInfoReq(mobile={ "value":"19000100002","valid":True},
    #                                         name={"value":"啦啦啦","valid":True},
    #                                         postion={"value":"总经理","valid":True},
    #                                         mail={"value":"18651085900@126.com","valid":True},
    #                                         qq={"value":"1314151","valid":True},
    #                                         concentration={"value":"13213131","valid":True},
    #                                         operation_remark={"value":"31231415","valid":True},
    #                                         record_id={"value":"47260","valid":True},
    #                                         user_id={"value":"100002","valid":True},
    #                                         logo={"value": "199241", "valid": True},
    #                                         wechat_qr_code={"value": "199241", "valid": True},
    #                                         company_name={"value": "199241", "valid": True},
    #                                         website={"value": "199241", "valid": True},
    #                                         telephone={"value": "199241", "valid": True},
    #                                         fax={"value": "199241", "valid": True},
    #                                         postcode={"value": "199241", "valid": True},
    #                                         biz_tel={"value": "199241", "valid": True},
    #                                         wechat={"value": "199241", "valid": True},
    #                                         weibo={"value": "199241", "valid": True},
    #                                         address={"value": "199241", "valid": True},
    #                                         province_code={"value": "199241", "valid": True},
    #                                         city_code={"value": "222", "valid": True}
    #
    #     ),metadata=self.metadata1
    # )
    #     self.assertEqual(self.response.success, True, "编辑用户信息接口错误")
    #
    # def test_case0003(self):
    #     '''添加公司信息'''
    #
    #     self.stub = comp_management_pb2_grpc.CompManagementServiceStub(self.channel)
    #     self.response = self.stub.AddCompanyInfo(
    #         comp_management_pb2.AddCompanyInfoReq(
    #                     company_id="G104411",
    #                     company_name= "深圳市冰融科技有限司",
    #                     company_type=1,
    #                     company_logo= "adafaafagg",
    #                     source= 1,
    #                     status=1,
    #                     created_by="阿的江"
    #     ),metadata=self.metadata1
    #
    #         )
    #     # print(self.response)
    #     self.assertEqual(self.response.success, True, "添加公司信息接口错误")
    #
    # def test_case0004(self):
    #     '''注册企业员工账号'''
    #
    #     self.stub = register_login_pb2_grpc.RegisterLoginServiceStub(self.channel)
    #     self.response = self.stub.RegisterEnterpriseEmployee(
    #         register_login_pb2.RegisterEnterpriseEmployeeReq(company_id="G151485", company_name="sdfsdf",
    #                                                          enterprise_type=1, register_ip="127.0.0.1",
    #                                                          user_info_list=[{"mobile": self.phone ,"name": "sdf",'password':'gys12356',"charge_region_codes":"222"}],
    #                                                          duplicate_registration_permitted=True
    #                                                          ), metadata=self.metadata1)
    #
    #     self.assertIsNotNone(self.response, "注册企业员工账号接口错误")
    #
    # def test_case0005(self):
    #     '''获取区域公司签约开发商列表'''
    #
    #     self.stub = comp_management_pb2_grpc.CompManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetCompContractListByAreaName(
    #         comp_management_pb2.GetCompContractListByAreaNameReq(
    #             contract_company='深圳分公司',
    #             page=1,
    #             page_size=10
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "获取区域公司签约开发商列表接口错误")
    #
    # def test_case0006(self):
    #     '''通过公司ID获取用户总数'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUserNumByCompanyId(
    #         user_management_pb2.GetUserNumByCompanyIdReq(
    #             company_id_list=["K007447", "K007823"],
    #             enterprise_type=1,
    #             search={"name": "吴"}
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过公司ID获取用户总数接口错误")
    #
    # def test_case0007(self):
    #     '''通过公司ID获取最新的用户信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetLatestUserInfoByCompanyId(
    #         user_management_pb2.GetLatestUserInfoByCompanyIdReq(
    #             company_id_list=["K007447", "K007823"],
    #             enterprise_type=2
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过公司ID获取最新的用户信息接口错误")
    #
    # def test_case0008(self):
    #     '''获取区域公司签约开发商列表'''
    #
    #     self.stub = comp_management_pb2_grpc.CompManagementServiceStub(self.channel)
    #     self.response = self.stub.GetCompContractListByAreaName(
    #         comp_management_pb2.GetCompContractListByAreaNameReq(
    #             contract_company='深圳分公司',
    #             page = 1,
    #             page_size = 10
    #         ),metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "注册企业员工账号接口错误")
    #
    # def test_case0009(self):
    #     '''通过公司ID获取混合型用户信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetMixedUserInfoByCompanyId(
    #         user_management_pb2.GetMixedUserInfoByCompanyIdReq(
    #             type=1,
    #             company_id="G092403",
    #             enterprise_type=1
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过公司ID获取混合型用户信息接口错误")
    #
    # def test_case0010(self):
    #     '''通过用户ID获取混合型用户信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetMixedUserInfoByUserId(
    #         user_management_pb2.GetMixedUserInfoByUserIdReq(
    #             type=1,
    #             user_id=["228098"],
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过用户ID获取混合型用户信息接口错误")
    #
    # def test_case0011(self):
    #     '''通过手机号或用户名称获取用户信息列表'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUserInfoListByMobileOrName(
    #         user_management_pb2.GetUserInfoListByMobileOrNameReq(
    #             mobile="13024082335",
    #             name="吴兴江",
    #             page=1,
    #             page_size=10
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过手机号或用户名称获取用户信息列表接错误")
    #
    # def test_case0012(self):
    #     '''通过用户ID列表批量获取用户信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUserInfoListByUserIdList(
    #         user_management_pb2.GetUserInfoListByUserIdListReq(
    #             user_id_list=["228098","227859"],
    #             page=1,
    #             page_size=10
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过用户ID列表批量获取用户信息接口错误")
    #
    # def test_case0013(self):
    #     '''通过手机号获取用户信息列表'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUserInfoListByMobile(
    #         user_management_pb2.GetUserInfoListByMobileReq(
    #         mobile="13024082335"
    #
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "通过手机号或用户名称获取用户信息列表接口错误")
    #
    # def test_case0014(self):
    #     '''通过用户ID判断当前用户是否为公司管理员'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetIsCompanyAdminByUserId(
    #         user_management_pb2.GetIsCompanyAdminByUserIdReq(
    #         user_id="198311",
    #         company_id="K006933"
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "通过用户ID判断当前用户是否为公司管理员接口错误")

    # def test_case0015(self):
    #     '''通过用戶ID解除绑定公司'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.UnbindCompanyByUserId(
    #         user_management_pb2.UnbindCompanyByUserIdReq(
    #             operator_user_id="224265",
    #             unbind_user_id="224265",
    #             unbind_user_name="啾啾"
    #
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "通过用戶ID解除绑定公司接口错误")

    # def test_case0016(self):
    #     '''通过TOKEN获取用户简要信息'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetUserProfileByToken(
    #         user_management_pb2.GetUserProfileByTokenReq(
    #             token="6f4b6f0f-f274-11ea-85b1-0242ac120002"
    #
    #
    #         ), metadata=self.metadata1
    #     )
    #     print(self.response)
    #     self.assertIsNotNone(self.response, "通过TOKEN获取用户简要信息接口错误")
    #
    #
    #
    # def test_case0017(self):
    #     '''将用户和（开发商/供应商）企业进行绑定'''
    #
    #     self.stub = user_management_pb2_grpc.UserManagementServiceStub(
    #         self.channel)
    #     self.response = self.stub.BindUserToCompany(
    #         user_management_pb2.BindUserToCompanyReq(
    #             user_id=self.phone,
    #             company_id='G159927',
    #             enterprise_type=1,
    #
    #
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "将用户和（开发商/供应商）企业进行绑定接口错误")
    #
    # def test_case0018(self):
    #     '''获取已绑定的用户的认证记录信息'''
    #
    #     self.stub = company_cert_pb2_grpc.CompanyCertServiceStub(
    #         self.channel)
    #     self.response = self.stub.GetBoundedUserCertificationInfoList(
    #         company_cert_pb2.GetBoundedUserCertificationInfoListReq(
    #             company_id="K006489",
    #             enterprise_type=1,
    #             page=1,
    #             page_size=10,
    #             user_id_list={"227850"}
    #         ), metadata=self.metadata1
    #     )
    #     # print(self.response)
    #     self.assertIsNotNone(self.response, "获取已绑定的用户的认证记录信息接口错误")

    def test_case0019(self):
        '''根据用户手机号发送验证码'''

        self.stub = user_management_pb2_grpc.UserManagementServiceStub(
            self.channel)
        self.response = self.stub.SendVerifyCode(
            user_management_pb2.SendVerifyCodeReq(
                phone="15827068970"
            ), metadata=self.metadata1
        )
        print(self.response)
        self.assertIsNotNone(self.response, "根据用户手机号发送验证码接口错误")





if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(user_center))
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # 实例化BeautifulReport模块
    run.report(filename='用户中心微服务接口测试报告', description='用户中心微服务接口')

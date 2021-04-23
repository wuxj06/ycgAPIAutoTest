import unittest
import requests
import random
from BeautifulReport import BeautifulReport


class OtherCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        list1 = list(range(10))
        a = '10' + str(random.choice(list1))
        b = ''.join(random.choice('0123456789') for j in range(8))
        cls.phone = a + b

    def test_case0001(cls):
        ''' 新增账号 '''

        cls.params = {
            "user_name": "mamba 4 life",
            "mobile": cls.phone,
            "position": "Shooting guard",
            "email": "24242424080808@qq.com",
            "qq": "24964149849"
        }
        cls.url = "https://micro-developer-api.b2bmir.com/v1/account-manager/add-account"
        cls.response = requests.post(
            url=cls.url,
            headers=cls.headers,
            data=cls.params
        )
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "新增账号")

    def test_case0002(cls):
        ''' 创建或编辑用户 '''

        cls.params = {
            "email": "12342515@qq.com",
            "framework_id": "5039",
            "mobile": "15988888888",
            "position": "岳父",
            "qq": "145566666",
            "user_id": "228098",
            "user_name": "接口自动化专用"
        }
        cls.url = "https://micro-developer-api.b2bmir.com/v1/organization/save-user"
        cls.response = requests.post(
            url=cls.url,
            headers=cls.headers,
            data=cls.params
        )
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "创建或编辑用户")

    def test_case0003(cls):
        ''' 新增招标管理员 '''

        cls.params = {
            "user_ids[0]": "228207"
        }
        cls.url = "https://micro-developer-api.b2bmir.com/v1/account-manager/add-business-admin"
        cls.response = requests.post(
            url=cls.url,
            headers=cls.headers,
            data=cls.params
        )
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "新增招标管理员")

    def test_case0004(cls):
        ''' 移除招标管理员 '''

        cls.params = {
            "user_id": "228207"
        }
        cls.url = "https://micro-developer-api.b2bmir.com/v1/account-manager/remove-business-admin"
        cls.response = requests.post(
            url=cls.url,
            headers=cls.headers,
            data=cls.params
        )
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "移除招标管理员")

    def test_case0005(cls):
        '''保存联盟配置信息'''

        cls.params = {
            "key": "skin",
            "value[mainColor]": "#ff6000"

        }
        cls.response = requests.post(
            url="https://m.b2bmir.com/api/web/league-config/save-league-config",
            headers=cls.headers,
            data=cls.params)
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(
            cls.dict1["success"],
            True,
            "保存联盟配置信息接口错误")

    def test_case0006(cls):
        '''获取供应商经营数据（经营异常，违法）'''

        cls.params = {
            "company_name": "富思特新材料科技发展股份有限公司"
        }
        cls.response = requests.get(
            url="https://opencenter.b2bmir.com/v1/supplier/base-data",
            params=cls.params)
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "获取供应商经营数据接口错误")

    def test_case0007(cls):
        '''供应商基础信息（标签，战略合作，荣誉，案例）'''

        cls.params = {
            "company_name": "富思特新材料科技发展股份有限公司"
        }
        cls.response = requests.get(
            url="https://opencenter.b2bmir.com/v1/supplier/base-data",
            params=cls.params)
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(
            cls.dict1["success"],
            True,
            "供应商基础信息（标签，战略合作，荣誉，案例）接口错误")

    def test_case0008(cls):
        '''校验供应商数据是否更新（基础信息、经营数据）'''

        cls.params = {
            "company_names[]": "上海三菱电梯有限公司",
            "start_time": "2020 - 06 - 13 20: 29:41"
        }
        cls.response = requests.post(
            url="https://opencenter.b2bmir.com/v1/supplier/check-data",
            data=cls.params)
        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(
            cls.dict1["success"],
            True,
            "校验供应商数据是否更新（基础信息、经营数据）接口错误")

    def test_case0009(cls):
        '''招募分享授权'''

        cls.params = {
            "c_nonce": "1606383238192sqh5uti93ko",
            "c_nonce_token": "94d2404e08353715eb118c7725ac0846",
            "item_ids": ["61738"],
            "user_ids": ["229601"],
        }
        cls.url = "https://m.b2bmir.com/api/kfsBackStage/recruit/save-permission"
        cls.response = requests.post(
            url=cls.url,
            headers=cls.headers,
            json=cls.params)

        cls.dict1 = dict(cls.response.json())
        print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
        cls.assertEqual(cls.dict1["success"], True, "招募分享授权接口错误")

    # def test_case0010(cls):
    #     ''' 供应商获取联系人(带搜索功能) '''
    #
    #     cls.params = {
    #         "supplierName" : "公司",
    #         "name" : "吴"
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/web/my-supplier/search-contacts"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "供应商获取联系人(带搜索功能) ")
    #
    # def test_case0011(cls):
    #     ''' 获取入库弹窗信息 '''
    #
    #     cls.params = {
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/web/my-supplier/get-confirm-storage-info?from_type=1&company_name=深圳市栾冰然卫浴"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "获取入库弹窗信息")
    #
    # def test_case0012(cls):
    #     ''' 项目列表接口 '''
    #
    #     cls.params = {
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/web/new-supplier-archive/get-win-supplier-project-list?supplierId=G161700&type=1&keywords="
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "项目列表接口")
    #
    # def test_case0013(cls):
    #     ''' 模糊查询已认证供应商 '''
    #
    #     cls.params = {
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/v2/developer/dim-search?keywords=公司&page_size=5"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "模糊查询已认证供应商")
    #
    # def test_case0014(cls):
    #     ''' 开发商官网招标-列表页接口 '''
    #
    #     cls.params = {
    #     "developer_id":"K006504"
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/subscribe/bidding/list"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "开发商官网招标-列表页接口")
    #
    # def test_case0015(cls):
    #     ''' 招标详情'''
    #
    #     cls.params = {
    #
    #     }
    #     cls.url = "https://m.b2bmir.com/api/subscribe/bidding/bidding-detail?uid=85253"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "招标详情")
    #
    # def test_case0016(cls):
    #     ''' 供应商模糊搜索'''
    #
    #     cls.params = {
    #         "keyword" : "园林"
    #     }
    #     cls.url = "https://m.b2bmir.com/api/miniProgram/supplier/suggest"
    #     cls.response = requests.get(
    #         url=cls.url,
    #         headers=cls.headers,
    #         data=cls.params
    #     )
    #     cls.dict1 = dict(cls.response.json())
    #     print(cls.dict1, '\n'"入参：", cls.params, '\n', "接口链接：", cls.url)
    #     cls.assertEqual(cls.dict1["success"], True, "供应商模糊搜索")
    # def test_case0001(cls):
    #     ''' 获取配置信息接口 '''
    #
    #     cls.params = {
    #
    #     }
    #
    #     cls.response = requests.get(
    #         url="https://" +
    #         cls.domain +
    #         "/api/web/config/get-config",
    #         headers=cls.headers)
    #     cls.dict1 = dict(cls.response.json())
    #     cls.assertEqual(cls.dict1["success"], True, "获取配置信息接口错误")
    #
    # def test_case0002(cls):
    #     '''保存联盟成员logo'''
    #
    #     cls.params = {
    #         "logo": "D:\"",
    #         "file_name": "55"
    #     }
    #     cls.response = requests.post(
    #         url="https://" +
    #         cls.domain +
    #         "/api/web/league-config/save-member-logo",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #
    #     cls.assertEqual(
    #         cls.dict1["success"],
    #         True,
    #         "保存联盟成员logo接口错误")
    #

    #
    # def test_case0004(cls):
    #     '''删除联盟成员logo'''
    #
    #     cls.params = {
    #         "logo_id": "sad",
    #
    #
    #     }
    #     cls.response = requests.post(
    #         url="https://" +
    #             cls.domain +
    #             "/api/web/league-config/delete-member-logo",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #
    #     cls.assertEqual(
    #         cls.dict1["success"],
    #         True,
    #         "删除联盟成员logo接口错误")
    #
    # def test_case0005(cls):
    #     ''' 获取联盟成员logo '''
    #
    #     cls.params = {
    #
    #     }
    #
    #     cls.response = requests.get(
    #         url="https://" +
    #         cls.domain +
    #         "/api/web/league-config/get-member-logo-list",
    #         headers=cls.headers)
    #     cls.dict1 = dict(cls.response.json())
    #     cls.assertEqual(cls.dict1["success"], True, "获取联盟成员logo接口错误")
    #
    # def test_case0006(cls):
    #     ''' 获取联盟皮肤配色信息 '''
    #
    #     cls.params = {
    #
    #     }
    #
    #     cls.response = requests.get(
    #         url="https://" +
    #         cls.domain +
    #         "/api/web/league-config/get-skin-config",
    #         headers=cls.headers)
    #     cls.dict1 = dict(cls.response.json())
    #     cls.assertEqual(cls.dict1["success"], True, "获取联盟皮肤配色信息接口错误")
    #
    # def test_case0007(cls):
    #     ''' 获取联盟页脚设置 '''
    #
    #     cls.params = {
    #
    #     }
    #
    #     cls.response = requests.get(
    #         url="https://" +
    #         cls.domain +
    #         "/api/web/league-config/get-footer-config",
    #         headers=cls.headers)
    #     cls.dict1 = dict(cls.response.json())
    #     cls.assertEqual(cls.dict1["success"], True, "获取联盟页脚设置接口错误")
    #
    # def test_case0008(cls):
    #     '''保存招标帮助'''
    #
    #     cls.params={
    #         "type":1,
    #         "file_id":11,
    #         "file_name":"1111"
    #     }
    #
    #     cls.response = requests.post(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/save-bidding-help",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "保存招标帮助接口错误")
    #
    # def test_case0009(cls):
    #     '''删除招标帮助文档'''
    #
    #     cls.params={
    #
    #         "file_id":11,
    #
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/del-bidding-help",
    #         headers=cls.headers,
    #         params=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "删除招标帮助文档接口错误")
    #
    # def test_case0010(cls):
    #     '''获取招标帮助列表'''
    #
    #     cls.params={
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/get-bidding-help-list",
    #         headers=cls.headers,
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "删除招标帮助文档接口错误")
    #
    # def test_case0011(cls):
    #     '''保存公告'''
    #
    #     cls.params={
    #         "name":"没病走两步啊啊啊",
    #         "content":"走两步就走两步"
    #     }
    #
    #     cls.response = requests.post(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/save-notice",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "保存公告接口错误")
    #
    # def test_case0012(cls):
    #     '''获取公告'''
    #
    #     cls.params={
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/get-notice",
    #         headers=cls.headers,
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "获取公告接口错误")
    #
    # def test_case0013(cls):
    #     '''保存颜色设置'''
    #
    #     cls.params={
    #         "skin_key":"green"
    #     }
    #
    #     cls.response = requests.post(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/save-skin",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "保存颜色设置接口错误")
    #
    # def test_case0014(cls):
    #     '''获取颜色设置'''
    #
    #     cls.params={
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/get-skin",
    #         headers=cls.headers,
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "获取颜色设置接口错误")
    #
    # def test_case0015(cls):
    #     '''保存企业专区图片'''
    #
    #     cls.params={
    #         "file_id":11,
    #         "file_name":111
    #     }
    #
    #     cls.response = requests.post(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/save-flagship-img",
    #         headers=cls.headers,
    #         data=cls.params)
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "保存企业专区图片接口错误")
    #
    # def test_case0016(cls):
    #     '''获取企业专区图片'''
    #
    #     cls.params={
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/get-flagship-img",
    #         headers=cls.headers,
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "获取企业专区图片接口错误")
    #
    # def test_case0017(cls):
    #     '''删除企业专区图片'''
    #
    #     cls.params={
    #         "img_id":"5305"
    #     }
    #
    #     cls.response = requests.get(url="https://" +
    #         cls.domain +
    #         "/api/kfsBackStage/exhibition-hall/del-flagship-img",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "删除企业专区图片接口错误")
    #
    # def test_case0018(cls):
    #     '''删除项目'''
    #
    #     cls.params={
    #          "id":66804
    #     }
    #
    #     cls.response = requests.get(url="https://micro-developer-api.b2bmir.com/v1/project/del-project",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "删除项目接口错误")
    #
    # def test_case0019(cls):
    #     '''项目列表'''
    #
    #     cls.params={
    #     "framework_id":""
    #     }
    #
    #     cls.response = requests.get(url="https://micro-developer-api.b2bmir.com/v1/project/get-project-list",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "项目列表接口错误")
    #
    # def test_case0020(cls):
    #     '''项目详情'''
    #
    #     cls.params={
    #         "id":66801
    #     }
    #
    #     cls.response = requests.get(url="https://micro-developer-api.b2bmir.com/v1/project/get-project-detail",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "项目列表接口错误")
    #
    # def test_case0021(cls):
    #     '''保存项目信息'''
    #
    #     cls.params={
    #         "id":"",
    #         "name":cls.data["auth-token"],
    #         "sub_company_id":"5039",
    #         "province":"111",
    #         "city":"112",
    #         "manager_ids":"228098"
    #     }
    #
    #     cls.response = requests.post(url="https://micro-developer-api.b2bmir.com/v1/project/save-project",
    #         headers=cls.headers,
    #         data=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "项目列表接口错误")
    #
    # def test_case0022(cls):
    #     '''创建或编辑用户'''
    #
    #     cls.params={
    #         "user_id":"227714",
    #         "user_name":"吴兴江dev",
    #         "mobile":"13024082335",
    #         "position":"111",
    #         "email":"11211111@qq.com",
    #         "qq":"2280981111"
    #     }
    #
    #     cls.response = requests.post(url="https://micro-developer-api.b2bmir.com/v1/organization/save-user",
    #         headers=cls.headers,
    #         data=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "创建或编辑用户接口错误")
    #
    # def test_case0023(cls):
    #     '''获取用户列表'''
    #
    #     cls.params={
    #         "page":1,
    #         "page_size":10
    #     }
    #
    #     cls.response = requests.get(url="https://micro-developer-api.b2bmir.com/v1/organization/get-user-list",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "获取用户列表接口错误")
    #
    # def test_case0024(cls):
    #     '''获取公司管理员信息'''
    #
    #     cls.params={
    #
    #     }
    #
    #     cls.response = requests.get(url="https://micro-developer-api.b2bmir.com/v1/organization/get-admin-info",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "获取公司管理员信息接口错误")
    #
    # def test_case0025(cls):
    #     '''通过token获取用户信息'''
    #
    #     cls.params={
    #         "token":cls.data["auth-token"]
    #     }
    #
    #     cls.response = requests.get(url="https://m.b2bmir.com/api/user/profile",
    #         headers=cls.headers,
    #         params=cls.params
    #         )
    #     cls.dict1 = dict(cls.response.json())
    #     # print(cls.dict1)
    #     cls.assertEqual(cls.dict1["success"], True, "通过token获取用户信息接口错误")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromTestCase(OtherCase))
    # unittest.TextTestRunner(verbosity=2).run(test_suite)
    run = BeautifulReport(test_suite)  # 实例化BeautifulReport模块
    run.report(filename='测试报告', description='综合招标单表标段全流程')

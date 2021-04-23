# import requests
# import json
# import encodings
#
# params = {
#     "app_id":"czy_test_id",
#     "app_secret":"czy_test_secret"
# }
# response1 = requests.post(url = "https://openapi.mycaigou.com/v1/login/token",
#                           data = params)
# dict1 = dict(response1.json())
# data1 = dict1["data"]
# token = data1["token"]
#
# tempParams =  {"user_name" : "lmh",
# "supplierName" :"hahahah",
# "url" : "http://www.baidu.com"
# }
# str = json.dumps(tempParams)
# body = {        "type" : "3",
#                 "content" : "不必惊慌，这是一条测试短信！",
#                 "phone" : "13077847823",
#                 "templateType":"1",
#                 "tempKey" : "company-audit-success-sms",
#                 "tempParams":str}
#
# response = requests.post(url="https://openapi.mycaigou.com/v1/sendsms/send?access-token="+token,
#                          data=body)
#
# print(response.json())
# params = {
#             "mobile": "13024242424",
#             "password": "kfs123456"
#         }
# url = "https://m.b2bmir.com/api/user/login/login-by-password"
# response = requests.post(url=url, json=params)
# dict1 = dict(response.json())
# data = dict1["data"]
# print(data["auth-token"])
# headers = {
#             "auth-token": data["auth-token"],
#             "Content-Type": "application/x-www-form-urlencoded"
#         }
#
# headers1={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#                          "auth-token": data["auth-token"]}
#
# params1={
#                 "company_name": "广东合和建筑五金制品有限公司",
#                 "from_type": "4",
#                 "contact_user_id": "227850",
#                 "user_name": "勿用吴兴江接口测试专用账号",
#                 "postion": "接口自动化",
#                 "mobile": "13024242424",
#                 "telephone": "",
#                 "category_str": "地坪漆,普通涂料,真石漆,普通涂料",
#                 "tag_str":""
#             }
#
# # dict1 = dict(response.json())
# url ="https://m.b2bmir.com/api/web/my-supplier/submit-storage-info"
# #requests.options(url, headers1)
# response = requests.post(url, params1, headers=headers1)
# dict1 = dict(response.json())
# print(response)
# # assertEqual(dict1["success"], True, "直接入库弹窗提交API错误")

__author__ = 'liuc22'
import register_login_pb2
import register_login_pb2_grpc
import grpc
import hmac
import time
from hashlib import sha256


def run():
    format = "%Y-%m-%d %H:%M:%S"
    t = time.strftime(format, time.localtime())
    timeArray = time.strptime(t, format)
    timeStamp = str(int(time.mktime(timeArray)))
    #timeStamp = '1597231871'
    app_id = 'micro-supplier-service'
    app_key = '748e4880546c5004d0164d70ce8df743'
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
    channel = grpc.insecure_channel('47.101.38.159:31009')
    metadata1 = (
        ('authorization', 'bearer %s.{"app_id":"micro-supplier-service","time_stamp":%s}' %(key, timeStamp)), )

    stub = register_login_pb2_grpc.RegisterLoginServiceStub(channel)
    response = stub.RegisterEnterpriseEmployee(
    register_login_pb2.RegisterEnterpriseEmployeeReq(company_id="G151485",company_name= "sdfsdf",enterprise_type= 1,register_ip="127.0.0.1",
                                                     user_info_list=[{"mobile": "19988855544", "name": "sdf"}]
                                                     ),metadata=metadata1)
    print(auth)
    print(key)
    print("Greeter client received: " + str(response))

if __name__ == "__main__":
    run()






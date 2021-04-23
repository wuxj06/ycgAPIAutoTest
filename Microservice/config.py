__author__ = 'wuxj06'
import os

base_dir = os.path.split(os.path.realpath(__file__))[0].replace('common', '')
proto_dir = base_dir + r'\proto'
filenames = os.listdir(proto_dir)
report_dir = base_dir + '\\report'


filenames = ["access_token.proto",'message.proto','message_name_config.proto','message_partner_config.proto','message_queue.proto','message_sms.proto','message_template.proto']
for flie in filenames:
    os.popen("python -m grpc_tools.protoc -I=D:\Python\python-api-common-protos-master --python_out=D:\Python --grpc_python_out=D:\Python -I=D:\\message_center\msn-service-center-proto\msn %s"%flie)

# for循环一次编译proto文件夹里面的proto文件，然后将生成python文件存放到项目文件夹根目录
# for file in filenames:
#     filename = file
#     os.popen(
#         r'python -m grpc_tools.protoc -I=D:\Python36\\api-common-protos --python_out=%s --grpc_python_out=%s  -I=%s %s' %
#         (base_dir, base_dir, proto_dir, filename))

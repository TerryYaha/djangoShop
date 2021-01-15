import json
import os

from django.http import HttpResponse

from djangoShop.dto.JsonMsg import JsonMsg
from djangoShop.settings import BASE_DIR
# def doFileUpload(request):
#     # 1.获取文件对象
#     fileInfo = request.FILES.get('aaa')
#     # 2.创建一个文件用来存放文件信息
#     # os.path.join 就是做路径拼接的方法，其中BASE_DIR就是你项目所在的系统路径，后面可以跟着无数个数据
#     # fileInfo.name 就是从上传上来的文件对象中获取文件名的信息
#     # wb：写入，并且按照字节的方式进行写入
#     f = open(os.path.join(BASE_DIR, "static", "file", fileInfo.name), 'wb')
#     # 3.开始讲fileInfo内容复制到f对象中，获取一个个字节信息，进行写入
#     for chunk in fileInfo.chunks():
#         f.write(chunk)

def doFileUpload(request):
    # 1.获取文件对象
    fileInfo = request.FILES.get('aaa')
    # 2.创建一个文件用来存放文件信息
    # os.path.join 就是做路径拼接的方法，其中BASE_DIR就是你项目所在的系统路径，后面可以跟着无数个数据
    # fileInfo.name 就是从上传上来的文件对象中获取文件名的信息
    # wb：写入，并且按照字节的方式进行写入
    f = open(os.path.join(BASE_DIR, "static", "file", fileInfo.name), 'wb')
    # 3.开始讲fileInfo内容复制到f对象中，获取一个个字节信息，进行写入
    for chunk in fileInfo.chunks():
        f.write(chunk)
    f.close()
    print('文件保存成功')

    jsonMsg = JsonMsg()
    jsonMsg.id = 1
    jsonMsg.msg = '文件上传成功'
    return HttpResponse(json.dumps(jsonMsg.__dict__, ensure_ascii=False))
    pass















































































    f.close()
    print('文件保存成功')

    jsonMsg = JsonMsg()
    jsonMsg.id = 1
    jsonMsg.msg = '文件上传成功'
    return HttpResponse(json.dumps(jsonMsg.__dict__, ensure_ascii=False))
    pass
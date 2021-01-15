import json

from django.http import HttpResponse

from djangoShop.dao.UserDao import UserDao
from djangoShop.dto.JsonMsg import JsonMsg

userInfoDao =UserDao()
def login(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    print(name,pwd)
    userInfo = userInfoDao.selectByNameAndPwd(name,pwd)

    jm = JsonMsg()
    if userInfo != None:
        request.session["admin"] = userInfo.__dict__
        #session'只能存放字典，字符串，数字类型，当不能放对象
        #session 不能存放日期类型信息，需要换成字符串或空值
        jm.id = 1
        jm.msg = "登录成功，即将跳转主页面"
        jm.location = "/index/"
    else:
        jm.id = 0
        jm.msg = "登录失败，用户名或密码有误"
    # 判断userInfo != None

    # 将数据发送回去，
    # 参数1：其实就是json的字符串
    # 参数2：返回数据的格式
    return HttpResponse(json.dumps(jm.__dict__,ensure_ascii=False), content_type="application/json")

#管理人员登录
def doAdminLogin(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    print(name,pwd)
    adminInfo = userInfoDao.selectAdminByNameAndPwd(name,pwd)
    jm = JsonMsg()
    if adminInfo != 0:
        request.session["manger"] = json.dumps(adminInfo.__dict__,ensure_ascii=False)
        #session'只能存放字典，字符串，数字类型，当不能放对象
        #session 不能存放日期类型信息，需要换成字符串或空值
        jm.id = 1
        jm.msg = "登录成功，即将跳转客服聊天"
        jm.location = "/servers/"
    else:
        jm.id = 0
        jm.msg = "登录失败，用户名或密码有误"
        print(111)
    return HttpResponse(json.dumps(jm.__dict__,ensure_ascii=False), content_type="application/json")

def doRegist(request):
    print("注册执行了")
    uName = request.POST.get("uname")
    uPwd = request.POST.get("uPwd")

    uEmail = request.POST.get("uEmail")
    uAddress = request.POST.get("uAddress")
    uPhone = request.POST.get("uPhone")
    userName = request.POST.get("userName")
    money = 0
    jm = JsonMsg()
    isPhone = userInfoDao.selectIsPhone(uPhone)
    print(bool(isPhone))
    if bool(isPhone) == False:
        userInfo = userInfoDao.insertUser(uName,uPwd,uEmail,uPhone,uAddress,money,userName)
        if userInfo != None:
            jm.msg = "恭喜您，注册成功！！请回首页登录"
            # jm.location = "/head/"
        else:
            # jm.id = 0
            jm.msg = "注册失败"
    else:
        jm.msg = "该手机号已被注册,请重新注册"

    return HttpResponse(json.dumps(jm.__dict__, ensure_ascii=False), content_type="application/json")


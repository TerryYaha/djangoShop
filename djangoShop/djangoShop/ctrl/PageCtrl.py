#此页面专门用来作为页面跳转
import json
from django.shortcuts import render
#到时候django会帮助我们调用这个方法，然后传入request对象
# request对象：当我们知道浏览器在提交数据的时候，发送了很多参数，这些参数存在request中

# 登录页
from pymysql.constants.FIELD_TYPE import JSON


def loginPage(request):
    #参数1：告诉系统要发送html的话，按照request（请求对象）的编码信息，发回去
    #参数2：返回的html名字，系统会自动去templates文件夹帮你找到这个文件发出去
    userInfo = request.session.get("admin")
    return render(request,"login.html",{"user":userInfo})

def adminLoginPage(request):
    return render(request, "adminLogin.html")
# 首页
def indexPage(request):
    userInfo = request.session.get("admin")
    return render(request,"index.html",{"user":userInfo})
# 会员信息
def myinfoPage(request):
    userInfo = request.session.get("admin")
    return render(request,"myInfo.html",{"user":userInfo})
# 订单页
def orderPage(request):
    userInfo = request.session.get("admin")
    #render检查内容是否有{}变量，如果有则修改ss
    return render(request,"order.html",{"user":userInfo})

# 注册页面
def registPage(request):
    #render检查内容是否有{}变量，如果有则修改ss
    return render(request,"regist.html")

# 购物车页
def cartPage(request):
    userInfo = request.session.get("admin")
    # order_state = request.
    return render(request,"cart.html",{"user":userInfo})

# 会员中心
def servicePage(request):
    userInfo = request.session.get("admin")
    return render(request,"service.html",{"user":userInfo})

def detailPage(request):
    num = request.GET['a']
    userInfo = request.session.get("admin")
    return render(request,"detail.html",{"num":num,"user":userInfo})

# def file(request):
#     return render(request, "file.html")

def exit(request):
    del request.session['admin']
    userInfo = None
    return render(request, "index.html",{"user":userInfo})

# def toDetail(request):
#     return render(request, "detail.html")
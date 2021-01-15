from django.shortcuts import render

from djangoShop.ctrl.XlsUtil import XlsUtil


def servicesPage(request):
    XlsUtil().readXls("message.xls")
    adminInfo = request.session.get("manger")
    return render(request, 'ServiceDemo.html',{"admin":adminInfo})

def userPage(request):
    userInfo = request.session.get("admin")
    return render(request, 'UserDemo.html',{"user":userInfo})

def userPage2(request):
    return render(request, 'UserDemo2.html')
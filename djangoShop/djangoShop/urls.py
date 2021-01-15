"""djangoShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path

from djangoShop.ctrl.CarInfoCtrl import *
from djangoShop.ctrl.OrderInfoCtrl import *
from djangoShop.ctrl.PageCtrl import *
from djangoShop.ctrl.PageHandler import *
from djangoShop.ctrl.fielCtrl import doFileUpload
from djangoShop.ctrl.proCtrl import *
from djangoShop.ctrl.userInfoCtrl import *
from django.contrib.staticfiles.views import serve


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginPage),
    url('^$',indexPage),
    path('index/',indexPage),
    path('order/',orderPage),
    path('cart/',cartPage),
    path('doLogin/',login),
    path('regist/',registPage),
    path('myInfo/',myinfoPage),
    path('doRegist/',doRegist),
    path('doFileUpload/',doFileUpload),
    path('service/',servicePage),
    path('proPage/',proPage),
    # 管理员登录页
    path('adminLogin/',adminLoginPage),
    path('doAdminLogin/',doAdminLogin),
    # 详情页
    path('detail/',detailPage),
    # 退出
    path('doExit/',exit),
    # 详情页数据渲染
    path('doDetail/',doDetail),
    # 订单页数据展示
    path('doOrder/',doOrder),
    # 购物车添加功能
    path('addCart/',addCart),
    # 购物车内容展示
    path('doCart/',doCart),
    # 取消订单
    path('delOrder/',delOrder),
    path('toBuy/',toBuy),
    # 删除购物车订单
    path('toDeleteBuy/',toDeleteBuy),
    # 订单支付功能
    path('payOrder/',payOrder),
    # 购物车支付功能
    path('payBuyCar/',payBuyCar),
    # 服务页面信息获取
    path('myService/',myService),
    # 余额充值
    path('investMoney/',investMoney),
    # 个人信息加载
    path('myInfoInit/',myInfoInit),
    # 个人信息更新
    path('updateInfo/',updateInfo),
    path('servers/', servicesPage),
    path('user/', userPage),
    # path('user2/', userPage2),
    # path('filePage/',file),
    # path('doFileUpload/',doFileUpload),
    # #订单购买
    # path('orderBuy/',orderBuy),
    url(r'^detail/?a=(\d+)/$', detailPage),
    re_path(r'^static/(?P<path>.*)$', return_static),
]



def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)




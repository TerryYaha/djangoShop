import json
from datetime import datetime

from django.http import HttpResponse

from djangoShop.dao.OrderInfoDao import OrderInfoDao
from djangoShop.dao.UserDao import UserDao
from djangoShop.dto.JsonMsg import JsonMsg

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)


def payBuyCar(request):
    print("购物车计算中。。。")
    userInfo = request.session.get('admin')
    buy_ids = request.GET.get("buy_id")#获取的是id数组
    buy_id = buy_ids.split(",")
    sum_price = request.GET.get("sum_price")
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location = '/login/'
    else:
        uid = userInfo['uid']

        # 插入预定购物车
        jsonMsg.id = 1
        orderInfoDao = OrderInfoDao()
        userInfoDao = UserDao()
        state = 2
        if len(buy_id)>0:
            orderId = datetime.now().strftime('%Y%m%d%H%M%S%f')
            u_money = userInfoDao.selectMoneyById(uid)
            # 金额充值时
            if int(u_money) >= int(sum_price):
                for i in range(0,len(buy_id)):

                    orderInfoDao = OrderInfoDao()
                    goodsCar = orderInfoDao.selectCarById(buy_id[i])
                    goodsCar = goodsCar[0].__dict__
                    print(goodsCar)
                    goods = orderInfoDao.insertOrderGoods(orderId,goodsCar["goodsId"], goodsCar["goodsName"], goodsCar["goodsPrice"], goodsCar["goodsImg"], goodsCar["goodsNum"])
                    carInfo = orderInfoDao.deleteCarInfo(uid,buy_id[i])
                    index = userInfoDao.updateMoneyByUid(sum_price, uid)
                index = orderInfoDao.insertOrderInfo(orderId, state, uid, sum_price)
                jsonMsg.msg = '订单购买成功'
            else:
                jsonMsg.msg = '很抱歉您的余额不足，请到会员中心页面充值'
        else:
            jsonMsg.msg = '您当前未选择商品'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder, ensure_ascii=False))


def myService(request):
    print("个人订单展示中。。。")
    userInfo = request.session.get('admin')

    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location = '/login/'
    else:
        uid = userInfo['uid']

        # 插入预定购物车
        jsonMsg.id = 1
        orderInfoDao = OrderInfoDao()
        userInfoDao = UserDao()
        money = userInfoDao.selectMoneyById(uid)
        print(money)
        jsonMsg.datas.append(money)

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder, ensure_ascii=False))

def investMoney(request):
    print("正在充值。。。")
    userInfo = request.session.get('admin')
    money = request.GET.get("money")
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location = '/login/'
    else:
        uid = userInfo['uid']

        jsonMsg.id = 1
        userInfoDao = UserDao()
        index = userInfoDao.addMoneyByUid(money,uid)
        jsonMsg.msg = '恭喜您，充值成功！'+'本次交易:'+money+'元'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder, ensure_ascii=False))

# 个人信息请求
def myInfoInit(request):
    print("个人信息加载。。。")
    userInfo = request.session.get('admin')
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location = '/login/'
    else:
        uid = userInfo['uid']
        jsonMsg.id = 1
        userInfoDao = UserDao()
        index = userInfoDao.selectUserById(uid)
        jsonMsg.datas.append(index.__dict__)
        jsonMsg.msg = '信息加载成功'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder, ensure_ascii=False))

def updateInfo(request):
    print("个人信息更新。。。")
    userInfo = request.session.get('admin')
    jsonMsg = JsonMsg()
    uname = request.POST.get("uname")
    uemail = request.POST.get("uemail")
    utel = request.POST.get("utel")
    userName = request.POST.get("userName")
    uaddr = request.POST.get("uaddress")

    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location = '/login/'
    else:
        uid = userInfo['uid']
        jsonMsg.id = 1
        userInfoDao = UserDao()
        index = userInfoDao.updateInfo(uname,uemail,utel,uaddr,userName,uid)
        if index > 0:
            jsonMsg.msg = '信息保存成功'
    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder, ensure_ascii=False))
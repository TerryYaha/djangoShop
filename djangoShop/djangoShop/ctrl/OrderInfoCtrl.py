from datetime import datetime
import json

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

def toBuy(request):
    print("购买，进入订单。。")
    gid = request.GET.get('goods_id')
    goods_price = request.GET.get('goods_price')
    goods_name = request.GET.get('goods_name')
    goods_img = request.GET.get('goods_img')
    goods_num = request.GET.get('goods_num')
    order_price = int(goods_num)*int(goods_price)
    #1.判断是否登陆过，如果没有返回错误信息

    userInfo = request.session.get('admin')
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        uid = userInfo['uid']
        # 插入预定购物车
        jsonMsg.id = 1

        # 1---未支付   2---已支付   3---退款
        state = 1
        orderId = datetime.now().strftime('%Y%m%d%H%M%S%f')
        orderInfoDao = OrderInfoDao()
        index = orderInfoDao.insertOrderInfo(orderId,state,uid,order_price)
        goods = orderInfoDao.insertOrderGoods(orderId,gid,goods_name,goods_price,goods_img,goods_num)
        if index and goods > 0:
            jsonMsg.msg = '即将进入订单页请支付'
            jsonMsg.location = '/order/'
        else:
            jsonMsg.msg = '添加失败'

    return HttpResponse(json.dumps(jsonMsg.__dict__, ensure_ascii=False))

def doOrder(request):
    print("订单显示执行")
    userInfo = request.session.get('admin')
    orderNum = request.GET.get("orderNum")
    start = request.GET.get('start')
    limit = request.GET.get('limit')
    print(start)
    print(limit)
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        uid = userInfo['uid']
        # 插入预定购物车
        jsonMsg.id = 1
        orderInfoDao = OrderInfoDao()
        orders = orderInfoDao.selectByPage(uid,int(start),int(limit),orderNum)
        count = orderInfoDao.countByPage(uid,orderNum)
        for item in orders:
            jsonMsg.datas.append(item.__dict__)
        jsonMsg.msg = '订单成功'
        jsonMsg.counts = count

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

def delOrder(request):
    orderId = request.GET.get("orderId")
    orderInfoDao = OrderInfoDao()
    order = orderInfoDao.deleteOrder(orderId)
    orderGoods = orderInfoDao.deleteOrderGoods(orderId)
    jsonMsg = JsonMsg()
    jsonMsg.msg = '订单取消成功'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

# 加入购物车
def addCart(request):
    print("正在执行加入购物车")
    userInfo = request.session.get('admin')
    goodsId = request.GET.get("goods_id")
    goods_price = request.GET.get('goods_price')
    goods_name = request.GET.get('goods_name')
    goods_img = request.GET.get('goods_img')
    goods_num = request.GET.get('goodsNum')
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        uid = userInfo['uid']
        # 插入预定购物车
        jsonMsg.id = 1
        orderInfoDao = OrderInfoDao()
        index = orderInfoDao.insertCar(uid,goodsId,goods_name,goods_img,goods_price,goods_num)

        if index >0:
            jsonMsg.msg = '加入购物车成功'
            jsonMsg.location = '/cart/'
        else:
            jsonMsg.msg = '加入购物车失败'


    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

def doCart(request):
    print("正在加载购物车数据")
    userInfo = request.session.get('admin')
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        uid = userInfo['uid']
        start = 0
        limit = 3
        # 插入预定购物车
        jsonMsg.id = 1
        orderInfoDao = OrderInfoDao()
        orders = orderInfoDao.selectCarByPage(uid,start,limit)
        count = orderInfoDao.countCarByPage(uid)
        for item in orders:
            jsonMsg.datas.append(item.__dict__)
        jsonMsg.msg = '购物车数据加载成功'
        jsonMsg.counts = count

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

def payOrder(request):
    print("订单支付中")
    orderNum = request.GET.get('orderNum')
    orderPrice = request.GET.get('orderPrice')
    userInfo = request.session.get('admin')
    # uid = userInfo['uid']
    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        # 插入预定购物车
        jsonMsg.id = 1
        state = 2
        uid = userInfo['uid']
        orderInfoDao = OrderInfoDao()
        userInfoDao = UserDao()
        u_money = userInfoDao.selectMoneyById(uid)
        if int(u_money) >= int(orderPrice):
            order = orderInfoDao.updateByState(state,orderNum)
            index = userInfoDao.updateMoneyByUid(orderPrice,uid)
            jsonMsg.msg = '订单购买成功'
        else:
            jsonMsg.msg = '您的余额不足，请到会员服务进行页面充值'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

# 订单购买
def orderBuy(request):
    print("订单购买中")
    orderId = request.POST.get('orderId')
    userInfo = request.session.get('admin')
    # uid = userInfo['uid']

    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:

        # 插入预定购物车
        jsonMsg.id = 1
        state = 2
        orderInfoDao = OrderInfoDao()
        print(orderId)
        index = orderInfoDao.updateByState(state,orderId)
        if index > 0:
            jsonMsg.msg = '订单购买成功'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))

def toDeleteBuy(request):
    print("购物车删除中。。")
    userInfo = request.session.get('admin')
    buyId = request.GET.get("buyId")

    jsonMsg = JsonMsg()
    if userInfo == None:
        jsonMsg.id = 0
        jsonMsg.msg = '请先登录'
        jsonMsg.location ='/login/'
    else:
        # 插入预定购物车
        jsonMsg.id = 1
        uid = userInfo['uid']
        orderInfoDao = OrderInfoDao()
        index = orderInfoDao.deleteCarInfo(uid,buyId)
        jsonMsg.msg = '购物车删除成功'

    return HttpResponse(json.dumps(jsonMsg.__dict__, cls=DateEncoder,ensure_ascii=False))
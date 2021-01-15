import json
from django.http import HttpResponse

from djangoShop.ctrl.OrderInfoCtrl import DateEncoder
from djangoShop.dao.GoodsInfoDao import GoodsInfoDao
from djangoShop.dto.JsonMsg import JsonMsg


def proPage(request):
    print("数据执行了")
    start = request.POST.get('start')
    limit = request.POST.get('limit')
    pro = request.POST.get('pro')

    goodsInfoDao = GoodsInfoDao()
    goods = GoodsInfoDao.selectByPage(int(start),int(limit),pro)

    count = goodsInfoDao.countByPage(pro)
    jsonMsg = JsonMsg()
    for item in goods:
        jsonMsg.datas.append(item.__dict__)
    jsonMsg.counts = count

    return HttpResponse(json.dumps(jsonMsg.__dict__, ensure_ascii=False))

# 详情页显示
def doDetail(request):
    print("详情页数据加载。。。")
    gid = request.GET.get("a")
    goodsInfoDao = GoodsInfoDao()
    pro = goodsInfoDao.selectById(gid)

    jsonMsg = JsonMsg()
    jsonMsg.datas.append(pro.__dict__)
    return HttpResponse(json.dumps(jsonMsg.__dict__, ensure_ascii=False))
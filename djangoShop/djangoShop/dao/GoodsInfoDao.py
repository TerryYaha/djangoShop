from djangoShop.model.GoodsInfo import GoodsInfo
from djangoShop.util.ConnUtil import ConnUtil

class GoodsInfoDao():
    def __init__(self):
        pass

    @classmethod
    def selectByPage(self,start,limit,content):
        connection = ConnUtil().getConn()
        sql = "select * from goods_info where 1 = 1 " #多条件查询的sql一定要加上where 1=1,并且后面要加上空格
        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        datas = ()
        #判断搜索的条件是否有值，如果有就添加sql以及查询的数据
        if content != None and content != '':
            sql = sql+' and goods_name like %s '
            #注意：元组的拼接需要,(逗号)
            datas = datas+( '%' + content + '%',)

        sql = sql + ' limit %s, %s '
        datas = datas + (start, limit)

        # print(sql,datas)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchall()
        # print(arr)
        connection.commit()
        connection.close()

        #数据整理，将整理后的数据return
        goods = []
        for index in range(len(arr)):
            t = GoodsInfo(arr[index][0],arr[index][1],arr[index][2],arr[index][3],
                           arr[index][4],arr[index][5],arr[index][6],arr[index][7],)
            goods.append(t)
        return goods
        pass

    @classmethod
    def selectById(self,gid):
        connection = ConnUtil().getConn()
        sql = "select * from goods_info where goods_id = %s " #多条件查询的sql一定要加上where 1=1,并且后面要加上空格
        datas = (gid,)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchall()

        connection.commit()
        connection.close()
        t = GoodsInfo(arr[0][0],arr[0][1],arr[0][2],arr[0][3],
                       arr[0][4],arr[0][5],arr[0][6],arr[0][7])
        return t
        pass

    def countByPage(self,content):
        connection = ConnUtil.getConn(self)
        sql = ' select count(*) from goods_info where 1 = 1 '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        datas = ()
        #判断搜索的条件是否有值，如果有就添加sql以及查询的数据
        if content != None and content != '':
            sql = sql+'and goods_name like %s'
            datas = datas+( '%' + content + '%',)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchone()
        # print(arr)
        connection.commit()
        connection.close()
        return arr[0]

# #测试
# dao = TicketInfoDao()
# dao.selectByPage(0,5,'厦门','福州')
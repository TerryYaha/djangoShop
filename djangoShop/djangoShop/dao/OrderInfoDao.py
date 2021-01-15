from djangoShop.model.GoodsCarInfo import GoodsCarInfo
from djangoShop.model.OrderInfo import OrderInfo
from djangoShop.util.ConnUtil import ConnUtil


class OrderInfoDao():
    def __init__(self):
        pass

    def insertOrderInfo(self,order_num,state,uid,order_price):
        connection = ConnUtil.getConn(self)
        sql = """
            insert into order_info (order_id,order_num,order_ctime,order_state,user_id,order_price)
            values
            (null,%s,now(),%s,%s,%s)
        """
        cursor = connection.cursor()
        cursor.execute(sql,(order_num,state,uid,order_price))
        index = cursor.rowcount
        connection.commit()
        connection.close()
        return index

    def insertOrderGoods(self,order_num,goods_id,goods_name,goods_price,goods_img,goods_num):
        connection = ConnUtil.getConn(self)
        sql = """
            insert into order_goods (order_goods_id,order_num,goods_id,goods_name,goods_price,goods_img,goods_num)
            values
            (null,%s,%s,%s,%s,%s,%s)
        """
        cursor = connection.cursor()
        cursor.execute(sql,(order_num,goods_id,goods_name,goods_price,goods_img,goods_num,))

        index = cursor.rowcount
        connection.commit()
        connection.close()
        return index

    def selectByPage(self,uid,start,limit,orderNum):

        connection = ConnUtil.getConn(self)
        sql = "select * from order_info as o,order_goods as g where o.order_num = g.order_num "
        datas = ()

        if (uid != None and uid != 0):
            sql = sql + " and o.user_id = %s "
            datas = datas + (uid,)
        if (orderNum != None and orderNum != 0):
            sql = sql + " and o.order_num like %s "
            datas = datas+( '%' + orderNum + '%',)
        sql = sql + "limit %s,%s"
        datas = datas + (start,limit)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchall()
        connection.commit()
        connection.close()


        #数据整理
        orderInfos = []

        for index in range(len(arr)):
            orderInfo = OrderInfo(arr[index][12],arr[index][6],arr[index][7],arr[index][8],
                                  arr[index][9],arr[index][10],arr[index][11],
                                  arr[index][0],arr[index][2],
                                  arr[index][3],arr[index][5])
            orderInfos.append(orderInfo)
        return orderInfos

    def countByPage(self,uid,orderNum):
        connection = ConnUtil.getConn(self)
        sql = ' select count(*) from order_info where 1 = 1 '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        datas = ()
        if orderNum != None and orderNum != '':
            sql = sql+'and order_num like %s'
            datas = datas+( '%' + orderNum + '%',)
        if (uid != None and uid != 0):
            sql = sql + " and user_id = %s"
            datas = datas + (uid,)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchone()
        # print(arr)
        connection.commit()
        connection.close()
        return arr[0]

    # 执行商品加入购物车功能
    def insertCar(self,uid,gid,gname,gimg,gprice,gnum):
        connection = ConnUtil.getConn(self)
        sql = """
            insert into buy_car (buy_id,user_id,goods_id,goods_name,goods_img,goods_price,buy_ctime,goods_num)
            values
            (null,%s,%s,%s,%s,%s,now(),%s)
        """
        cursor = connection.cursor()
        cursor.execute(sql,(uid,gid,gname,gimg,gprice,gnum))
        index = cursor.rowcount
        connection.commit()
        connection.close()
        return index

    def selectCarByPage(self,uid,start,limit):

        connection = ConnUtil.getConn(self)
        sql = "select * from buy_car where 1 = 1 "
        datas = ()

        if (uid != None and uid != 0):
            sql = sql + " and user_id = %s "
            datas = datas + (uid,)

        sql = sql + "limit %s,%s"
        datas = datas + (start,limit)
        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchall()
        connection.commit()
        connection.close()

        #数据整理
        goodsCarInfos = []
        for index in range(len(arr)):
            goodsCarInfo = GoodsCarInfo(arr[index][0],arr[index][1],arr[index][2],
                                  arr[index][3],arr[index][4],arr[index][5],
                                  arr[index][6],arr[index][7])
            goodsCarInfos.append(goodsCarInfo)
        return goodsCarInfos

    # 格局购物车id查询
    def selectCarById(self,buyId):
        connection = ConnUtil.getConn(self)
        sql = "select * from buy_car where buy_id = %s "
        datas = ()
        datas = datas + (buyId,)
        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchall()
        connection.commit()
        connection.close()

        #数据整理
        # print(arr)
        goodsCarInfos = []
        for index in range(len(arr)):
            goodsCarInfo = GoodsCarInfo(arr[index][0],arr[index][1],arr[index][2],
                                  arr[index][3],arr[index][4],arr[index][5],
                                  arr[index][6],arr[index][7])
            goodsCarInfos.append(goodsCarInfo)
        return goodsCarInfos

    def countCarByPage(self,uid):
        connection = ConnUtil.getConn(self)
        sql = ' select count(*) from buy_car where 1 = 1 '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        datas = ()
        if (uid != None and uid != 0):
            sql = sql + " and user_id = %s"
            datas = datas + (uid,)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchone()
        connection.commit()
        connection.close()
        return arr[0]

    def deleteCarInfo(self,uid,buyId):
        connection = ConnUtil.getConn(self)
        sql = ' DELETE FROM buy_car WHERE buy_id = %s '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        datas = ()
        datas = datas + (int(buyId),)
        if (uid != None and uid != 0):
            sql = sql + " and user_id = %s"
            datas = datas + (uid,)

        cursor = connection.cursor()
        cursor.execute(sql,datas)
        arr = cursor.fetchone()
        connection.commit()
        connection.close()
        return arr

    def deleteOrder(self,orderId):
        connection = ConnUtil.getConn(self)
        sql = ' DELETE FROM order_info WHERE order_num = %s '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        # datas = ()
        # datas = datas + (orderId,)
        cursor = connection.cursor()
        cursor.execute(sql,orderId)
        arr = cursor.fetchone()
        connection.commit()
        connection.close()
        # print(arr)
        return arr

    def deleteOrderGoods(self,orderId):
        connection = ConnUtil.getConn(self)
        sql = ' DELETE FROM order_goods WHERE order_num = %s '

        #定义一个元组变量,到时候我需要的数据（查询的数据）存放在里面
        cursor = connection.cursor()
        cursor.execute(sql,orderId)
        arr = cursor.fetchone()
        connection.commit()
        connection.close()
        # print(arr)
        return arr
    #
    # def selectById(self,tid):
    #     connections = ConnUtil.getConn()
    #     sql = "select * from ticket_info where tid = %s"
    #     cursor = connections.cursor()
    #     cursor.execute(sql,(tid,))
    #     ticket = cursor.fetchone()
    #     connections.commit()
    #     connections.close()
    #     t = TicketInfo(ticket[0],ticket[1],ticket[2],ticket[3],
    #                    ticket[4],ticket[5],ticket[6],ticket[7])
    #     return t
    #

    # 改变订单状态
    def updateByState(self,state,orderNum):
        connections = ConnUtil.getConn(self)
        sql = "update order_info set order_state = %s where order_num = %s "
        cursor = connections.cursor()
        cursor.execute(sql,(state,orderNum))
        t = cursor.rowcount
        connections.commit()
        connections.close()
        return t
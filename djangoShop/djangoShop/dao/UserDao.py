#Dao  D:Data  a:access访问  o：object    即数据访问用户
from djangoShop.model.AdminInfo import AdminInfo
from djangoShop.model.UserInfo import UserInfo
from djangoShop.util.ConnUtil import ConnUtil


class UserDao():
    def __init__(self):
        self.flag = 0
        pass;
    def selectUserById(self,uid):
        #1.获取连接
        connection = ConnUtil.getConn(self)
        #2.编写sql语句
        sql = "select * from user_info where user_id = %s "
        #3.获取解析对象，此解析对象用来判断sql语法是否有误，以及到时候参数传入是否有误
        cursor = connection.cursor()
        #4.开始执行sql语句
        cursor.execute(sql,(uid,))
        #5.获取数据
        arr = cursor.fetchall()
        # print(arr)
        #6提交刚刚的搜索信息
        connection.commit()
        #7.关闭连接
        connection.close()

        user = []
        user = UserInfo(arr[0][0], arr[0][1], arr[0][2], arr[0][3],
                           arr[0][4],arr[0][5],arr[0][6],arr[0][7])
        return user

    def selectByNameAndPwd(self,name,pwd):
        #1.获取连接
        connection = ConnUtil.getConn(self)
        #2.编写sql语句
        sql = "select * from user_info where user_name = %s and user_pwd = %s "
        #3.获取解析对象，此解析对象用来判断sql语法是否有误，以及到时候参数传入是否有误
        cursor = connection.cursor()
        #4.开始执行sql语句
        cursor.execute(sql,(name,pwd))
        #5.获取数据
        arr = cursor.fetchall()
        # print(arr)
        #6提交刚刚的搜索信息
        connection.commit()
        #7.关闭连接
        connection.close()
        user = []
        user = UserInfo(arr[0][0], arr[0][1], arr[0][2], arr[0][3],
                           arr[0][4],arr[0][5],arr[0][6],arr[0][7])
        return user

    def selectAdminByNameAndPwd(self,name,pwd):
        #1.获取连接
        connection = ConnUtil.getConn(self)
        #2.编写sql语句
        sql = "select * from admin_info where admin_name = %s and admin_pwd = %s "
        #3.获取解析对象，此解析对象用来判断sql语法是否有误，以及到时候参数传入是否有误
        cursor = connection.cursor()
        #4.开始执行sql语句
        cursor.execute(sql,(name,pwd))
        #5.获取数据
        arr = cursor.fetchall()
        #6提交刚刚的搜索信息
        connection.commit()
        #7.关闭连接
        connection.close()
        if bool(arr) == False:
            admin = 0
        else:
            admin = []
            admin = AdminInfo(arr[0][0], arr[0][1], arr[0][2])
        return admin

    def insertUser(self,uname,upwd,uEmail,uphone,uAddress,money,userName):
        # 1.获取连接
        connection = ConnUtil().getConn();
        # 2.编写sql语句(千万别加分号，加了就死)
        sql = "insert into user_info(user_id,user_name,user_pwd,user_email,user_tel,user_addr,user_money,u_name) values (null, %s, %s,%s,%s, %s,%s,%s)"
        # 3.获取解析sql对象，这个解析对象用来判断sql是否语法有错，以及到时候参数传入是否有误
        cursor = connection.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (uname,upwd,uEmail,uphone,uAddress,money,userName))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        arr = cursor.rowcount
        # print(index)
        # 6.提交刚刚的搜索信息
        connection.commit()
        # 7.关闭连接
        connection.close()

        flag = 1
        # user = UserInfo(arr[0][0], arr[0][1], arr[0][2], arr[0][3],
        #                    arr[0][4],arr[0][5],arr[0][6],arr[0][7],arr[0][8],arr[0][9],arr[0][10],arr[0][11])
        return flag

    def loginUser(self, name, pwd):
        # 1.获取连接
        connection = ConnUtil().getConn();
        # 2.编写sql语句(千万别加分号，加了就死)
        sql = "select * from user where uname = %s and upwd = %s"
        # 3.获取解析sql对象，这个解析对象用来判断sql是否语法有错，以及到时候参数传入是否有误
        cursor = connection.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (name, pwd))
        arr = cursor.fetchall()

        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        if cursor.execute(sql, (name, pwd)):
            print("登陆成功")
        else:
            self.flag = 1
            print("登陆失败，输入不正确")
        # 6.提交刚刚的搜索信息
        connection.commit()
        # 7.关闭连接
        connection.close()


        user = []
        user = UserInfo(arr[0][0], arr[0][1], arr[0][2], arr[0][3],
                           arr[0][4],arr[0][5],arr[0][6],arr[0][7])
        return user

    def updateMoneyByUid(self,orderPrice,uid):
        connections = ConnUtil.getConn(self)
        sql = " update user_info set user_money = user_money -%s where user_id = %s"
        cursor = connections.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (orderPrice,uid))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        index = cursor.rowcount
        # print(index)
        # 6.提交刚刚的搜索信息
        connections.commit()
        # 7.关闭连接
        connections.close()
        return  index

    def updateInfo(self,uname,uemail,utel,uaddress,userName,uid):
        connections = ConnUtil.getConn(self)
        sql = " update user_info set user_name = %s,user_email = %s,user_tel = %s,user_addr = %s,u_name = %s where user_id = %s "
        cursor = connections.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (uname,uemail,utel,uaddress,userName,uid))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        index = cursor.rowcount
        # print(index)
        # 6.提交刚刚的搜索信息
        connections.commit()
        # 7.关闭连接
        connections.close()
        return  index

    def addMoneyByUid(self,money,uid):
        connections = ConnUtil.getConn(self)
        sql = " update user_info set user_money = user_money +%s where user_id = %s"
        cursor = connections.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (money,uid))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        index = cursor.rowcount
        # print(index)
        # 6.提交刚刚的搜索信息
        connections.commit()
        # 7.关闭连接
        connections.close()
        return  index

    def selectMoneyById(self,uid):
        connections = ConnUtil.getConn(self)
        sql = " select user_money from user_info where user_id = %s "
        cursor = connections.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (uid))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        money = cursor.fetchall()
        # print(index)
        # 6.提交刚刚的搜索信息
        connections.commit()
        # 7.关闭连接
        connections.close()
        return  money[0][0]

    # 查询注册手机号
    def selectIsPhone(self,uphone):
        connections = ConnUtil.getConn(self)
        sql = " select * from user_info where user_tel = %s "
        cursor = connections.cursor()
        # 4.开始执行sql语句
        cursor.execute(sql, (uphone))
        # 5.获取数据 rowcount：当执行增删改的时候，rowcount是获取修改的行数
        # row：行，count：数量
        arr = cursor.fetchall()
        # print(index)
        # 6.提交刚刚的搜索信息
        connections.commit()
        # 7.关闭连接
        connections.close()
        return  arr
# userDao = UserDao()
# userDao.selectAll()
import pymysql

class ConnUtil():
    def __init__(self):
        pass

    def getConn(self):
        connection = pymysql.Connect(
            host = "localhost",
            user = "root",
            password = "123",
            charset = "utf8",
            port = 3306,
            database = 'hf200915'
        )
        return connection
Util = ConnUtil()
print(Util.getConn())
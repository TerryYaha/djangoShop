class JsonMsg():
    def __init__(self):
        self.id = 0 #登录，判断是否成功，1：成功，0：失败
        self.msg = '' #发送给浏览器的信息，例如登录成功
        self.location = '' #用来保存跳转信息，例如登陆成功，跳转到主页面，这里设置为主页面的url
        self.datas = [] #用来保存分页数据
        self.counts = 0  # 保存信息条数
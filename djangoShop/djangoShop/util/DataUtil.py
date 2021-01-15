class DataUtil():
    # 客服发送信息send方法
    adminSendObj = None
    # 用户的send对象：
    # 格式：{‘name’:‘用户名’, ‘send’: send对象, 'talk': 聊天记录, 'state': 0或者1,0：客服，1：人工}
    userSendArr = []
    # 高亮用户
    lightUserName = None

    # 用户信息。只要用户上线，就将用户数据保存在该列表中
    userArr = []
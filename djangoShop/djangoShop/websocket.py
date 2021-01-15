import json
import time
from djangoShop.ctrl import RedisUtil
from djangoShop.util.DataUtil import DataUtil


async def websocket_application(scope, receive, send):
    # 开始死循环接收数据信息
    while True:
        event = await receive()  # 收到消息，这个收消息是阻塞型的函数，当收到消息时返回事件对象
        if event['type'] == 'websocket.connect':  # 用户信息连接上来了
            await send({'type': 'websocket.accept'})
        if event['type'] == 'websocket.disconnect':  # 断开链接的业务
            break
        if event['type'] == 'websocket.receive':  # 收到消息的业务
            dictObj = json.loads(event['text'])
            # 添加管理员的业务
            if dictObj['service'] == 'addAdmin':
                # 1.将客服数据保存起来,并且高亮取消
                DataUtil.adminSendObj = send
                DataUtil.lightUserName = None
                # 2.获取所有用户列表发送给客服，客服显示
                # 2.1.定义一个数组，用来存放用户名
                userArr = []
                if len(DataUtil.userSendArr) > 0 :
                    for item in DataUtil.userSendArr:
                        userArr.append(item['name'])
                # 2.2.将信息发送出去
                sendMessage = {'service':'userNames', 'content': userArr}
                await send({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})
            # 添加用户的业务
            if dictObj['service'] == 'addUser':
                # 1.将用户信息进行保存，但是需要判断之前是否有登录过，如果有则替换之前的信息, 如果没有则添加用户到聊天信息中
                hasLoginUser = False
                if len(DataUtil.userSendArr) > 0:
                    for item in DataUtil.userSendArr:
                        if item['name'] == dictObj['content']:
                            hasLoginUser = True
                            item['send'] = send
                if hasLoginUser == False: # 如果该用户都没有聊天过，那么就添加用户
                    DataUtil.userSendArr.append({'name': dictObj['content'], 'send': send, 'talk': [], 'state': 0})
                    # 如果客服登录过就直接发送给客服和客服说新增了
                    if DataUtil.adminSendObj != None:
                        # 发送用户上线的消息给服务页面,让服务器添加用户信息
                        sendMessage = {'service': 'addUser', 'content': dictObj['content']}
                        await DataUtil.adminSendObj({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})

            # 用户发送数据上来
            if dictObj['service'] == 'userSendMsg':
                userInfo = None
                # 1.找到用户信息
                if len(DataUtil.userSendArr) > 0:
                    for item in DataUtil.userSendArr:
                        if item['name'] == dictObj['who']:
                            userInfo = item

                # 切换模式
                if dictObj['content'] == '转人工':
                    userInfo['state'] = 1
                    sendDictObj = {'service': 'sendUserTip',
                                   'content': "已转为人工"}
                    await send({"type": "websocket.send", "text": json.dumps(sendDictObj, ensure_ascii=False)})
                else:
                    if userInfo['state'] == 0:
                        aiMsg = RedisUtil.readProp(dictObj['content'])
                        if aiMsg == None:
                            aiMsg = '抱歉，小库没听懂您的问题，请选择转人工'
                        # 保存信息
                        userInfo['talk'].append(dictObj['who'] + "说:" + dictObj['content'] + "\r\n")
                        userInfo['talk'].append("\n机器人:"+aiMsg + "\r\n")
                        # 将信息发送给客户端：
                        nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        sendMessage = {'service': 'sendUserMsg',
                                       'content': "\n"+nowtime+": "+dictObj['who'] + "说:" + dictObj['content'] + "\r\n"}
                        sendMessage1 = {'service': 'sendUserMsg',
                                       'content': "\n机器人:"+aiMsg + "\r\n"}

                        # 2.将信息发送给客服人员(如果高亮的正好是这个用户)
                        if DataUtil.adminSendObj != None:
                            if DataUtil.lightUserName != None and DataUtil.lightUserName == dictObj['who']:
                                await DataUtil.adminSendObj(
                                    {"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})
                                await DataUtil.adminSendObj(
                                    {"type": "websocket.send", "text": json.dumps(sendMessage1, ensure_ascii=False)})
                        # 3.将信息发给该用户
                        await send({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})
                        await send({"type": "websocket.send", "text": json.dumps(sendMessage1, ensure_ascii=False)})
                    else:
                        # 保存信息
                        userInfo['talk'].append(dictObj['who'] + "说:" + dictObj['content'] + "\r\n")
                        # 整理数据
                        sendMessage = {'service':'sendUserMsg', 'content':"\n"+nowtime+": "+ dictObj['who'] + "说:" +  dictObj['content'] + "\r\n"}
                        # 2.将信息发送给客服人员(如果高亮的正好是这个用户)
                        if DataUtil.adminSendObj !=None:
                            if DataUtil.lightUserName != None and DataUtil.lightUserName == dictObj['who']:
                                await DataUtil.adminSendObj({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})
                            else:
                                sendMessage2 = {'service':'tipMsg', 'content': dictObj['who'] + "有新消息，请查阅"}
                                await DataUtil.adminSendObj(
                                    {"type": "websocket.send", "text": json.dumps(sendMessage2, ensure_ascii=False)})
                        # 3.将信息发给该用户
                        await send({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})

            # 高亮
            if dictObj['service'] == 'lightUser':
                # 1.将高亮用户保存起来
                DataUtil.lightUserName = dictObj['content']
                # 2.获取这个高亮用户的所有聊天信息
                talk = None
                for item in DataUtil.userSendArr:
                    if item['name'] == dictObj['content']:
                        talk = item['talk']
                # 3.发送给服务器端
                sendMessage = {'service': 'sendTalks', 'content': talk }
                await DataUtil.adminSendObj({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})

            # 客服发送信息上来
            if dictObj['service'] == 'sendAdminMsg':
                # 定义一个变量用来保存用户send数据信息
                customSendObj = None
                # 1.将聊天信息保存到对应用户中
                if len(DataUtil.userSendArr) > 0:
                    for item in DataUtil.userSendArr:
                        if item['name'] == dictObj['who']:
                            item['talk'].append(dictObj['content'] + "\r\n")
                            customSendObj = item['send']
                # 2.将信息发送给服务人员
                sendMessage = {'service': 'sendUserMsg', 'content': dictObj['content'] + "\r\n"}
                await DataUtil.adminSendObj(
                    {"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})
                # 3.将信息发送给客户
                if customSendObj != None:
                    await customSendObj({"type": "websocket.send", "text": json.dumps(sendMessage, ensure_ascii=False)})

"""
ASGI config for project1223 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os

from django.core.asgi import get_asgi_application
# print("aaaa")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1223.settings')
# application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from djangoShop.websocket import websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoShop.settings')
django_application = get_asgi_application()
async def application(scope, receive, send):
    # 如果请求的类型是http
    if scope['type'] == 'http':
        # 调用django系统的函数进行应用
        await django_application(scope, receive, send)
    # 如果请求的类型是websocket
    elif scope['type'] == 'websocket':
        # 这个是我们自己定义的一个方法，需要在 项目名相同的包下创建一个py文件，这个py文件里面有websocket_application方法
        await websocket_application(scope, receive, send)
    # 如果都不是的话，那么就直接判断是未知请求信息
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")

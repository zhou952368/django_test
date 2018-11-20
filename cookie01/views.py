import datetime

from django.http import HttpResponse
from django.shortcuts import render

# 第一次请求服务器------>返回cookie信息
# 下次来的时候浏览器自带cookie信息  -----> 获取cookie信息
from django_test import settings

"""
设置
更新
删除
获取

作用域
过期时间

"""


def cookie01(request):
    response = HttpResponse('设置cookie信息')
    """
       
   参数说明
   key,   键
   value='',  值   默认的空字符串
   max_age=None,  设置过期时间   整形  单位是秒
   expires=None,   设置过期时间  时间类型  默认设置一年
   path='/',       限制获取cookie的路径
   domain=None,    设置子域名 能访问到cookie信息
   secure=False,    使用https协议的时候需要设置为True
   httponly=False   只能通过HTTP协议传输cookie信息   js无法操作cookie
   
   """
    # 设置cookie信息
    response.set_cookie('k1', 'hello', max_age=10)
    # 设置国际时间  单位是时间类型
    response.set_cookie('k2', 'hello', expires=datetime.timedelta(days=7))
    response.set_cookie('k3', 'hello', path='/cookie/set')
    response.set_cookie('k4', 'hello', domain='.baidu.com')
    return response


"""
安全问题  
数据量比较小
只能存ASC||
"""


def cookie02(request):
    # 获取cookie信息 如果key不存在就抛出异常
    v1 = request.COOKIES['k1']
    #  获取cookie信息  如果key不存在就返回None
    v3 = request.COOKIES.get('k1')
    response = HttpResponse('')
    response.set_signed_cookie('k4', '子威'.encode(), salt=settings.SECRET_KEY)
    return response


def session1(request):
    # ====设置操作
    # 如果key存在 则覆盖
    request.session['k1'] = '1'
    # 如果key存在  则不设置
    request.session.setdefault('k1', 1)
    # 获取操作
    # 如果key不存在就报错
    v = request.session['k1']
    # 如果key不存在就返回默认值 None 为人为设置的默认值
    v = request.session.get('k1', None)
    return HttpResponse('session操作')

import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import User


def index(request):
    return render(request, 'index.html')


def list(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')
        try:
            if re.match('^[A-Z]{1}[a-zA-Z0-9]{7,16}$', username) and len(password):
                users = User.objects.filter(username=username)
                if users.exists():
                    user = users.first()
                    if user.verify_password(password):
                        request.session['username'] = user.username
                        return render('/')
                    else:
                        return render(request, 'login.html', {'msg': '密码错误!!!'})

                else:
                    return render(request, 'login.html', {'msg': '用户名不存在'})

            else:
                return render(request, 'login.html', {'msg': '账号密码不符合规范'})

        except:
            return render(request, '404.html')
            # return HttpResponse('404')

    else:
        # 不支持请求方式
        pass


def register(request):
    user = User(username='Zhou123456')
    user.password = '123456'
    user.save()
    return HttpResponse('注册成功')


def logout(request):
    del request.session['username']
    return redirect('/')

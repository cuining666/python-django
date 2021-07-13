from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
import datetime
from blog import models


def indexPage(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {"now": now})
    # return HttpResponse('<h1>ok</h1>')


def userPage(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        name = request.POST.get("name", None)
        sex = request.POST.get("sex", None)
        # user = {"username": username, "name": name, "sex": sex}
        # user_list.append(user)
        # 新增数据
        models.UserInfo.objects.create(
            username=username,
            name=name,
            sex=sex
        )
    # 获取数据列表
    user_list = models.UserInfo.objects.all()
    return render(request, "userPage.html", {"user_list": user_list})


def noNameParams(request, arg1, arg2):
    return HttpResponse("id:" + arg1 + ", name:" + arg2)


def nameParams1(request, name, id):
    return HttpResponse("id:" + id + ", name:" + name)


def nameParams2(request, name):
    return HttpResponse("name:" + name)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        if username == 'admin' and pwd == 'admin':
            return HttpResponse("login success")
        else:
            return redirect("/blog/login")
    return render(request, "login.html")

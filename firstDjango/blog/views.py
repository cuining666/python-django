from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
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

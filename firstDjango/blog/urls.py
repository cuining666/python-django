# __author: ioi
# date: 2021/7/7
from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('now', views.indexPage),
    path('userInfo', views.userPage),
    # url中有正则表达式，则使用re_path
    re_path(r'^test1/(\d{4})/(\w{1,20})$', views.noNameParams),
    re_path(r'^test2/(?P<id>\d{4})/(?P<name>\w{1,20})$', views.nameParams1),
    path('index', views.nameParams2, {"name": "index"}),
    # url别名
    path('login', views.loginPage, name="login")
]

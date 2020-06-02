## 这是一个学习用的python项目
## 每天更新

## 简单的使用方法：

创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器


路由设置：

from django.conf.urls import url, include
from django.contrib import admin
from App import views

显示在最上方的链接处

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/',views.hello),
    url(r'^hehe/',views.hehe),
    url(r'^haha/',views.haha),
    url(r'^index/',views.index),
    url(r'^home/',views.home),
    url(r'^two/', include('Two.urls')),
]

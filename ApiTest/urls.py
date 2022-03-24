"""ApiTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path

from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),
    path('home/',home),
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$",child),
    path('login/',login),
    path('login_action/',login_action), # 登录
    path('register_action/',register_action), # 注册
    re_path(r'^accounts/login/$',login), # 非登录状态跳转回登录
    path('logout/',logout), # 退出
    path('pei/',pei), # 吐槽
    path('help/', api_help),# 帮助
    path('project_list/', project_list),# 项目列表
    path('interface/', interface),

]



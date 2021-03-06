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
    path('delete_project/', delete_project),# 删除项目
    path('add_project/', add_project),# 新增项目
    re_path(r'^apis/(?P<id>.*)/$',open_apis),# 接口库
    re_path(r'^cases/(?P<id>.*)/$',cases),# 用例设计
    re_path(r'^project_set/(?P<id>.*)/$',project_set),# 项目设置
    re_path(r'^save_project_set/(?P<id>.*)/$',save_project_set),# 保存项目设置
    re_path(r'^project_api_add/(?P<Pid>.*)/$',project_api_add), # 新增接口
    re_path(r'^project_api_del/(?P<id>.*)/$',project_api_del), # 删除接口
    path('save_bz/',save_bz),# 保存备注
    path('get_bz/',get_bz),# 获取备注

    path('interface/', interface),

]



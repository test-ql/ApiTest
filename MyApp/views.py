from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MyApp.models import *

# Create your views here.
@login_required
def welcome(request):
    return render(request,'welcome.html')

@login_required
def project_list(request):
    return render(request,'welcome.html',{'whichHTML':'project_list.html','oid':''})

def interface(request):
    return render(request,'interface.html')

@login_required
def api_help(request):
    return render(request,'welcome.html',{'whichHTML':'help.html','oid':''})

# 不同页面返回不同数据：数据分发器
def child_json(eid):
    if eid == 'home.html':
        date = DB_home_href.objects.all()
        res = {"hrefs":date}
        return res
    if eid == 'project_list.html':
        date = DB_project.objects.all()
        res = {"projects":date}
        return res

# 返回子页面
def child(request,eid,oid):
    res = child_json(eid)
    return render(request,eid,res)


@login_required
def home(request):
    return render(request,'welcome.html',{'whichHTML' : 'home.html',"oid":""})

def login(request):
    return render(request,'login.html')

def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    user = auth.authenticate(username = u_name,password = p_word)
    if user is not None:
        auth.login(request,user)
        request.session['user'] = u_name
        return HttpResponse('登录成功')
    else:
        return HttpResponse('登录失败')

def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    try:
        user = User.objects.create_user(username=u_name,password=p_word)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('用户名已存在，注册失败！')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def pei(request):
    tucao_text = request.GET['tucao_text']
    DB_tucao.objects.create(user=request.user.username,text=tucao_text)
    return HttpResponse('成功')





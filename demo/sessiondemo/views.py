from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# 设置session数据函数
def setsession(request):
    request.session['classname'] = 'python'
    return HttpResponse(setsession)

# 读取session值函数
def getsession(request):
    value = request.session['classname']
    print(value)
    return HttpResponse(getsession)
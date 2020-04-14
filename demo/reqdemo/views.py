import json

from django.http import HttpResponse
from django.shortcuts import render, redirect


# 查询字符串传参

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    lis = request.GET.getlist('b')
    print(a)
    print(b)
    print(lis)
    return HttpResponse('qsok')

# 通过 URL 路径传参,获取天气
def weather(request, city, year):
    print(f'city:{city}')
    print(f'year:{year}')
    return HttpResponse('weather')


# 表单类型类型参数 ( Form Data )
def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    lis = request.POST.getlist('a')
    print(a)
    print(b)
    print(lis)
    return HttpResponse('get_body')


# 非表单类型传值
def get_json(request):
    json_by = request.body
    json_str = json_by.decode()
    json_dirt = json.loads(json_str)
    a = json_dirt.get('a')
    b = json_dirt.get('b')
    print(a)
    print(b)
    return HttpResponse('get_body')


# 重定向
def ref(request):

    return redirect('/users/index/')

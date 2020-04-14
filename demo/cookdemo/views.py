from django.http import HttpResponse
from django.shortcuts import render


# 设置cookie函数
def set_cook(request):
    response = HttpResponse('set_cook')
    response.set_cookie('lhcc',' python')
    return response


# 读取cookie函数
def get_cook(request):
    data = request.COOKIES.get('lhcc')
    print(data)
    return HttpResponse('get_cook')
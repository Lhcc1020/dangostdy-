from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class RegisterView(View):
    """设置类视图处理注册"""

    def get(self, request):
        """处理get请求"""
        print('当前浏览器为get请求')
        return HttpResponse('当前浏览器为get请求')

    def post(self, request):
        print('当前浏览器为post请求')
        return HttpResponse('当前浏览器为post请求')

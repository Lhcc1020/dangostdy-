from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^setsession/$', views.setsession),
    re_path(r'^getsession/$', views.getsession),
]
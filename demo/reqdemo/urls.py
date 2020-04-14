from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^reqrest/$', views.qs),
    re_path(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
    re_path(r'^res/$', views.get_body),
    re_path(r'^bad/$', views.get_json),
]
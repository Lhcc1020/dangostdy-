from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('^setcook/$',views.set_cook),
    re_path('^getcook/$',views.get_cook),
]
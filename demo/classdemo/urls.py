from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path('^register/$',views.RegisterView.as_view()),
]
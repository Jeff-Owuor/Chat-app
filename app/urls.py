from django.urls import re_path,path,include
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^login',views.login,name='login'),
]
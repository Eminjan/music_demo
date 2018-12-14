#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django.urls import path
from . import views

# 设置首页的url地址信息
urlpatterns = [
    path('',views.indexView,name='index'),

]

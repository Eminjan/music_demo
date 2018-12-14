#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    # 用户的注册和登录
    path('login.html', views.loginView, name='login'),
    # 用户中心
    path('home/<int:page>.html', views.homeView, name='home'),
    # 退出用户登录
    path('logout.html', views.logoutView, name='logout'),
]
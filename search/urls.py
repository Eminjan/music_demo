#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django.urls import path
from . import views
urlpatterns = [
    path('<int:page>.html', views.searchView, name='search'),
]
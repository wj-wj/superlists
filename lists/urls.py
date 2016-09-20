#! /usr/bin/env python
# _*_coding:utf-8_*_

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
]
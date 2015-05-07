# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.user_login', name='login'),
    url(r'^logout/$', 'accounts.views.user_logout', name='logout'),
    url(r'^/$', 'accounts.views.home', name='home'),
)

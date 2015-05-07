# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agentV2.views.home', name='home'),
    url(r'^/', include('accounts.urls'),

    url(r'^admin/', include(admin.site.urls)),
)

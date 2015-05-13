# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.conf.urls import patterns, url


urlpatterns = patterns('accounts.views',
                       url(r'^login/$', 'user_login', name='login'),
                       url(r'^logout/$', 'user_logout', name='logout'),
                       url(r'^$', 'home', name='home'),
                       url(r'^qsProxy.html', 'show_qsproxy'),
                       )

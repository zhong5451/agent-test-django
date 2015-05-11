# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.conf.urls import patterns, url


urlpatterns = patterns('pay.views',
    url(r'^pay/', 'pay_by_alipay'),
    url(r'^nofify-async/', 'nofify_async'),
    url(r'^return/', 'return_func'),
)

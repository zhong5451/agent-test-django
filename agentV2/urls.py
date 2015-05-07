# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('accounts.urls')),
                       url(r'^pay', include('pay.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from settings import STATIC_URL, STATICFILES_DIRS

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('accounts.urls')),
                       url(r'^pay', include('pay.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
print STATIC_URL, STATICFILES_DIRS
urlpatterns += static(STATIC_URL, document_root=STATICFILES_DIRS[0])

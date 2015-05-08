# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from utils.helper import json_response
import urllib2


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print request.POST
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            print user.is_active
            if user.is_active:
                login(request, user)
                print reverse('home')
                return redirect(reverse('home'))
            else:
                return render(request, 'login.html',
                              {'error_msg': u'The user is not active.'})
        else:
            return render(request, 'login.html',
                          {'error_msg': u'Username or Password is error.'})
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect(reverse('login'))


@login_required(login_url=settings.LOGIN_URL)
def home(request):
    return render(request, 'home.html', {})

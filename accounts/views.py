# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

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
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('home'))
            else:
                return json_response({'msg': u'The user is not active.'})
        else:
            return json_response({'msg': u'Username or Password is error.'})
    else:
        print 1111
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def home(request):
    return render(request, 'home.html', {})

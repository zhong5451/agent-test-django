# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import requests
# import urllib
# import urllib2


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


@login_required
def home(request):
    url = 'http://10.18.103.31:8888/api/home/agent-user-login/'
    params = {'uname': request.user.username, 'uid': request.user.id}
    # params = urllib.urlencode(params)
    # req = urllib2.Request(url, params)
    # # urllib2.urlopen(req)
    # response = urllib2.urlopen(req)
    # result = response.read()
    r = requests.post(url, data=params)
    print r.text
    return render(request, 'home.html', {})

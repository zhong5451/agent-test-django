# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from django.http import HttpResponse
import simplejson as json


def json_response(data, error=False, **kwargs):
    response = HttpResponse(
               json.dumps(data, ensure_ascii=True),
               content_type='application/json')
    return response

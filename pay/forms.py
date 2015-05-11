# encoding: utf-8
'''
Created on 2015-05-11

@author: xiaowei
'''

from django import forms


class PaymentForm(forms.Form):
    total_fee = forms.FloatField(min_value=0.01, max_value=100000000.00)
    domain_buy = forms.CharField(min_length=3, max_length=1280)
    service = forms.IntegerField(min_value=1)
    # flag = forms.IntegerField(min_value=0, max_value=1)
    user_id = forms.IntegerField(min_value=0, max_value=1)
    out_trade_no = forms.CharField(max_length=32)
    subject = forms.CharField(max_length=64)
    body = forms.CharField(max_length=128)
    # sign = forms.CharField()

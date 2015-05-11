# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from django.http import HttpResponse
import simplejson as json


def json_response(data, error=False, **kwargs):
    response = HttpResponse(
               json.dumps(data, ensure_ascii=True),
               content_type='application/json')
    return response


def encrypt(text, private_key):
    # cryptor = AES.new(self.key, self.mode, b'0000000000000001')
    cryptor = AES.new(private_key, AES.MODE_ECB)
    # 这里密钥key 长度必须为16（AES-128）,
    # 24（AES-192）,或者32 （AES-256）Bytes 长度
    # 目前AES-128 足够目前使用
    length = 16
    count = len(text)
    if count < length:
        add = (length-count)
        # \0 backspace
        text = text + ('\0' * add)
    elif count > length:
        add = (length-(count % length))
        text = text + ('\0' * add)
    ciphertext = cryptor.encrypt(text)
    # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
    # 所以这里统一把加密后的字符串转化为16进制字符串
    return b2a_hex(ciphertext)


def get_clientip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        client_ip = request.META['REMOTE_ADDR']
    client_ips = client_ip.split(',')
    client_ip = client_ips[0]
    return client_ip

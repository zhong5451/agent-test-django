# encoding: utf-8
'''
Created on 2015-05-05

@author: xiaowei
'''

from alipay.create_direct_pay_by_user.forms import AliPayDirectPayForm
from alipay.helpers import make_sign, get_form_data
from decimal import Decimal
from django.conf import settings
from pay.forms import PaymentForm
from utils.helper import json_response
import urllib2
import uuid


def pay_by_alipay(request):
    form = PaymentForm(getattr(request, request.method))
    print form
    print form.is_valid()
    if not form.is_valid():
        return json_response({'status': 400})

    total_fee_form = form.cleaned_data.get('total_fee', 0.01)
    domain_buy = form.cleaned_data.get('domain_buy', '')

    # service_info = Service_rank_info.objects.all()
    # service_dict = {service.service_id: service for service in service_info}
    # sum total fee is correct?
    pay_url = 'http://%s' % settings.DOMAIN
    out_trade_no = uuid.uuid1().hex
    total_payments = Decimal(0)
    description_goods = u''

    # source_service = service_dict.get(item.service_version_id, {})
    # if not source_service:
    #     return qs_conf.RETURN_SERVICE_ERROR
    description_goods = u'为域名【%s】购买套餐【%s】' % (domain_buy,
                        'source_service.service_name')
    try:
        unit_price = int(100)
        quantity = int(3)
    except ValueError:
        return json_response({'status': 400})

    subject = u"青松抗D防御套餐"
    detail_body = description_goods

    # orders = Order_form.objects.filter(out_trade_no=out_trade_no, user=uid)
    # if not orders:
    #     order = Order_form.objects.create(out_trade_no = out_trade_no,
    #                                       user_id = uid,
    #                                       payment_money = Decimal(str(total_payments)),
    #                                       payment_way = qs_conf.order_form_payment_way[0],
    #                                       desc = detail_body,
    #                                       )
    #     order.save()

    # orders.update(payment_money=Decimal(str(total_payments)), desc = detail_body)

    # alipay form
    alipay_dict = {
            "_input_charset": 'utf-8',
            'notify_url': '%s/api/alipay/return_async/' % str(pay_url),
            #'return_url': '%s/api/alipay/return/' % pay_url,
            'sign_type': 'MD5',
            #'sign': '',
            #'error_notify_url': '',
            'out_trade_no': out_trade_no,
            'subject': subject,
            #'buyer_id': '',
            #'seller_account_name': '',
            #'buyer_account_name': '',
            'seller_email': settings.ALIPAY_SELLER_EMAIL,
            #'price': '',
            'total_fee': 220,
            #'quantity': '',
            #'it_b_pay': '1h',   # 超时时间m-分钟,h-小时,d-天,1c-当天(无论交易何时创建,都在 0 点关闭)。 该参数数值不接受小数点, 如1.5h,可转换为 90m
            'body': detail_body,
            #'show_url': '',
            #'discount': '',
            #'need_ctu_check': 'Y',
            #'royalty_type': '',
            #'royalty_parameters': '',
            'anti_phishing_key': 'AABBCDDEG',
            #'exter_invoke_ip': '',
            'extra_common_param': 'This is a test request',
            #'extend_param': '',
            'default_login': 'Y',
            #'product_type': '',
            #'token': '',
            }
    alipay_form = AliPayDirectPayForm(auto_id=False, initial=alipay_dict)
    data = get_form_data(alipay_form)
    alipay_form['sign'].field.initial = make_sign(data)
    data = get_form_data(alipay_form)
    request_url = alipay_form.get_action()
    for key, value in data.items():
        if isinstance(value, unicode):
            v = value.encode(alipay_form.initial['_input_charset'])
        else:
            v = value.decode('utf-8').encode(alipay_form.initial['_input_charset']) if hasattr(value, 'decode') else value
        try:
            v = urllib2.quote(v)
        except AttributeError:
            pass
        request_url += "&%s=%s" % (key, v)
    # return HttpResponseRedirect(request_url)
    return_data = {}
    return_data['alipay_url'] = request_url
    return_data.update()
    return json_response(return_data)

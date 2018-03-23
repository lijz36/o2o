#-*- coding: UTF-8 -*-
from django.db import models
from userinfo.models import UserInfo
from memberapp.models import Goods


ORDERSTATUS = (
		(1,"未支付",),
		(2,"已支付"),
		(3,"订单取消"),
	)


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id')
    good = models.ForeignKey(Goods, db_column='good_id')
    ccount = models.IntegerField('数量', db_column='cart_count')

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.ccount

    def get_absolute_url(self):
        return '???'

    class Meta():
        db_table = 'cartinfo'


class Order(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id')
    orderNo= models.CharField(max_length=200, verbose_name="订单号")
    ads= models.CharField(max_length=200, verbose_name="收件人")
    acot= models.CharField(max_length=200, verbose_name="总数")
    acounts= models.CharField(max_length=200, verbose_name="价格")
    cals = models.TextField(verbose_name="orderdetail",null=True, blank=True)
    orderStatus = models.IntegerField(verbose_name="订单状态", blank=True, choices=ORDERSTATUS, default='1')

    def __unicode__(self):
        return self.user
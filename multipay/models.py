# -*- coding:utf-8 -*-
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from enum import IntEnum


class GATEWAY_TYPE(IntEnum):
    PAYPAL = 2


GATEWAY_CHOICES = (
    (GATEWAY_TYPE.PAYPAL, _('Paypal')),
)


class Gateway(models.Model):
    # sid = models.CharField(max_length=8, default=short_uid, db_index=True)
    site = models.ForeignKey(Site, on_delete=models.DO_NOTHING, related_name='gateways')
    type = models.SmallIntegerField(choices=GATEWAY_CHOICES, )
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    note = models.CharField(max_length=250, null=True, blank=True, verbose_name=_('Note'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    default = models.BooleanField(default=True, verbose_name=_('Default'))
    archive = models.BooleanField(default=False, verbose_name=_('Archive'))


class TRANSACTION_STATUS(IntEnum):
    PENDING = 1
    FAILED = 2
    SUCCESS = 3
    CANCELED = 4
    REFUND = 5
    REFUND_COMPLETE = 6


TRANSACTION_STATUS_CHOICES = (
    (TRANSACTION_STATUS.PENDING, _('Pending')),
    (TRANSACTION_STATUS.FAILED, _('Failed')),
    (TRANSACTION_STATUS.SUCCESS, _('Success')),
    (TRANSACTION_STATUS.CANCELED, _('Canceled')),
    (TRANSACTION_STATUS.REFUND, _('Refund')),
    (TRANSACTION_STATUS.REFUND_COMPLETE, _('Refund complete')),
)


class Transaction(models.Model):
    # sid = models.CharField(max_length=40, default=long_uid, db_index=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    gateway = models.ForeignKey(Gateway, on_delete=models.DO_NOTHING, verbose_name=_('Gateway'))
    amount = models.FloatField(default=0, verbose_name=_('Amount'))
    status = models.SmallIntegerField(choices=TRANSACTION_STATUS_CHOICES, default=1, verbose_name=_('Status'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    modified = models.DateTimeField(auto_now_add=True, verbose_name=_('Modified'))
    # content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING, null=True, blank=True)
    # currency = models.CharField(verbose_name=_('Currency'), choices=CURRENCY_CHOICES, max_length=3)
    # object_id = models.PositiveIntegerField(default=0)
    # obj = GenericForeignKey('content_type', 'object_id')
    error_message = models.TextField(null=True, blank=True, verbose_name=_('Error message'))

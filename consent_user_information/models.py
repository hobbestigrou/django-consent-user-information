# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


class AbstractConsentUserInformation(models.Model):
    """An abstract model to extend easily the consent user information"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True, blank=True)
    device = models.CharField(max_length=100, blank=True)
    browser = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ConsentUserInformation(AbstractConsentUserInformation):
    """To store content user information"""
    pass

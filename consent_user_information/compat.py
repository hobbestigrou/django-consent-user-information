# -*- coding: utf-8 -*-
import django


def is_authenticated(user):
    """To check if the user is authenticated"""
    if django.VERSION >= (1, 10):
        return user.is_authenticated
    else:
        return user.is_authenticated()

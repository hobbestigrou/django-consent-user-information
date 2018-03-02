# -*- coding: utf-8 -*-
from django import forms


class MailForm(forms.Form):
    """docstring for MailForm"""
    mail = forms.EmailField(required=True)

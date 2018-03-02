# -*- coding: utf-8 -*-
from django.conf.urls import url

from tests.views import home_view, confirmation_view, simple_view

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^confirmation/$', confirmation_view, name='confirmation'),
    url(r'^simple/$', simple_view, name='simple')
]

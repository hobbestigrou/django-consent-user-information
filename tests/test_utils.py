# -*- coding: utf-8 -*-
import django

import pytest

from consent_user_information.utils import create_user_consent_information

if django.VERSION >= (1, 10):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


def test_without_user_agent(rf):
    request = rf.get(reverse('home'))

    with pytest.raises(ValueError):
        create_user_consent_information(request)

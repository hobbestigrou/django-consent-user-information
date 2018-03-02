# -*- coding: utf-8 -*-
import django

import pytest
from faker import Faker

from consent_user_information.models import ConsentUserInformation

if django.VERSION >= (1, 10):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_consent_user_information(client):
    fake = Faker()

    client.post(reverse('home'), {'mail': fake.email()})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user is None
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'


@pytest.mark.django_db
def test_consent_user_information_login(client, user, password):
    fake = Faker()

    client.login(username=user.username, password=password)
    client.post(reverse('home'), {'mail': fake.email()})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user == user
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'


@pytest.mark.django_db
def test_consent_user_information_mail(client, user):
    client.get(reverse('simple'), {'mail': user.email})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user == user
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'


@pytest.mark.django_db
def test_consent_user_information_user(client, user):
    client.get(reverse('simple'), {'user': user.pk})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user == user
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'

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
def test_consent_user_information_login(client, django_user_model):
    fake = Faker()
    username = fake.user_name()
    password = fake.password()
    user = django_user_model.objects.create(username=username)

    user.set_password(password)
    user.save()

    client.login(username=username, password=password)
    client.post(reverse('home'), {'mail': fake.email()})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user == user
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'


@pytest.mark.django_db
def test_consent_user_information_mail(client, django_user_model):
    fake = Faker()
    username = fake.user_name()
    password = fake.password()
    mail = fake.email()
    user = django_user_model.objects.create(username=username, email=mail)

    user.set_password(password)
    user.save()

    client.get(reverse('simple'), {'mail': mail})

    consent_user_information = ConsentUserInformation.objects.last()

    assert ConsentUserInformation.objects.count() == 1
    assert consent_user_information.user == user
    assert consent_user_information.ip == '127.0.0.1'
    assert consent_user_information.device == 'Other'
    assert consent_user_information.browser == 'Other'

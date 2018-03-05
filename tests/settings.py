# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os

import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = True
USE_TZ = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tests/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "&vd4&(kcl(oix+x=bdn$2_0mq5313n$*u^bcqw=fkp(x+1v%m)"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django_user_agents",
    "consent_user_information",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django_user_agents.middleware.UserAgentMiddleware',
        'consent_user_information.middleware.marketing'
    )
else:
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django_user_agents.middleware.UserAgentMiddleware',
        'consent_user_information.middleware.Marketing'
    )

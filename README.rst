=============================
django-consent-user-information
=============================

.. image:: https://img.shields.io/pypi/v/pymarvelsimple.svg
   :alt: Latest release on the Python Cheeseshop (PyPI)
   :target: https://pypi.python.org/pypi/django-consent-user-information

.. image:: https://travis-ci.org/hobbestigrou/django-consent-user-information.svg?branch=master
    :alt: Build status of perf on Travis CI
    :target: https://travis-ci.org/hobbestigrou/django-consent-user-information

A simple app to manage consent users information. Sometimes it's important to
store information from the user.

Documentation
-------------

The full documentation is at https://django-consent-user-information.readthedocs.io.

Quickstart
----------

Install django-consent-user-information::

    pip install django-consent-user-information

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_user_agents',
        'consent_user_information.apps.ConsentUserInformationConfig',
        ...
    )


After that use the mixin check the tests to see an example.

Features
--------

* Store information from the user, ip, browser and device

# -*- coding: utf-8 -*-
import logging

from django.contrib.auth import get_user_model

from ipware import get_client_ip

from consent_user_information.models import ConsentUserInformation
from consent_user_information.compat import is_authenticated

logger = logging.getLogger(__name__)


def create_user_consent_information(request, mail=None):
    """To create an user consent information"""
    if not hasattr(request, 'user_agent'):
        raise ValueError('Check if the middleware is present')

    data = {
        'device': request.user_agent.device.family,
        'browser': request.user_agent.browser.family
    }
    client_ip, is_routable = get_client_ip(request)

    if client_ip is None:
        logger.warning("Unable to get the ip")
    else:
        data['ip'] = client_ip

    if mail:
        data['user'] = get_user_model().objects.get(email=mail)
    else:
        if is_authenticated(request.user):
            data['user'] = request.user

    ConsentUserInformation.objects.create(**data)

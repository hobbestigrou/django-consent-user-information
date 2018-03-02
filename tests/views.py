# -*- coding: utf-8 -*-
import django
from django.views.generic import FormView, TemplateView
from django.contrib.auth.models import User

from consent_user_information.views import UserConsentUserInformationMixin
from consent_user_information.utils import create_user_consent_information
from tests.forms import MailForm

if django.VERSION >= (1, 10):
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse


class HomeView(UserConsentUserInformationMixin, FormView):
    """To display home"""
    template_name = 'simple/home.html'
    form_class = MailForm

    def get_success_url(self):
        """To get the url"""
        return reverse('confirmation')


class ConfirmationView(TemplateView):
    """To display confirmation"""
    template_name = 'simple/confirmation.html'


class SimpleView(TemplateView):
    """To display simple"""
    template_name = 'simple/simple.html'

    def get(self, request, *args, **kwargs):
        """Get the mail from url"""
        mail = request.GET.get('mail', None)

        if mail:
            create_user_consent_information(request, mail=mail)
        else:
            user = User.objects.get(pk=request.GET['user'])
            create_user_consent_information(request, user=user)

        return super(SimpleView, self).get(request, *args, **kwargs)


home_view = HomeView.as_view()
confirmation_view = ConfirmationView.as_view()
simple_view = SimpleView.as_view()

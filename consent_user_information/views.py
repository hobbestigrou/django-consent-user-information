# -*- coding: utf-8 -*-
from consent_user_information.utils import create_user_consent_information


class UserConsentUserInformationMixin(object):
    """A mixin to manage consent user information"""
    def form_valid(self, form):
        """Create the consent user information mixin if the form is valid"""
        create_user_consent_information(self.request)
        return super(UserConsentUserInformationMixin, self).form_valid(form)

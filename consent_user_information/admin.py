# -*- coding: utf-8 -*-
from django.contrib import admin

from consent_user_information.models import ConsentUserInformation


class ConsentUserInformationAdmin(admin.ModelAdmin):
    """Admin for consent user information"""
    list_display = ('user', 'ip', 'device', 'browser', 'created_at')
    list_select_related = ('user',)
    readonly_fields = ('user', 'ip', 'device', 'browser', 'created_at')
    search_fields = ['user__email', 'user__first_name', 'user__last_name']

    def has_add_permission(self, request):
        """Can't add a new entry"""
        return False


admin.site.register(ConsentUserInformation, ConsentUserInformationAdmin)

from django.conf import settings


CONSENT_USER_INFORMATION_KEY_SESSION = getattr(
    settings, 'CONSENT_USER_INFORMATION_KEY_SESSION',
    'consent_user_information_marketing')
CONSENT_USER_INFORMATION_UTM_SOURCE = getattr(
    settings, 'CONSENT_USER_INFORMATION_UTM_SOURCE', 'utm_source')
CONSENT_USER_INFORMATION_UTM_MEDIUM = getattr(
    settings, 'CONSENT_USER_INFORMATION_UTM_MEDIUM', 'utm_medium')
CONSENT_USER_INFORMATION_UTM_CONTENT = getattr(
    settings, 'CONSENT_USER_INFORMATION_UTM_CONTENT', 'utm_content')

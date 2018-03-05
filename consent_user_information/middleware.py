from consent_user_information.conf import (
    CONSENT_USER_INFORMATION_KEY_SESSION, CONSENT_USER_INFORMATION_UTM_SOURCE,
    CONSENT_USER_INFORMATION_UTM_MEDIUM, CONSENT_USER_INFORMATION_UTM_CONTENT)


def _set_session_marketing(request):
    marketing_name = [
        CONSENT_USER_INFORMATION_UTM_SOURCE,
        CONSENT_USER_INFORMATION_UTM_MEDIUM,
        CONSENT_USER_INFORMATION_UTM_CONTENT
    ]
    marketing = {}

    for name in marketing_name:
        utm_value = request.GET.get(name, None)

        if utm_value:
            marketing[name] = utm_value

    request.session[CONSENT_USER_INFORMATION_KEY_SESSION] = marketing


def marketing(get_response):
    """To manage marketing information"""
    def middleware(request):
        """Get marketing information from the url and stored in the session"""
        _set_session_marketing(request)

        response = get_response(request)

        return response
    return middleware


class Marketing(object):
    """To manage marketing information"""
    def process_request(self, request):
        """Get marketing information from the url and stored in the session"""
        _set_session_marketing(request)

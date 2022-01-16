from django.shortcuts import get_object_or_404

from cookies.forms import AllCookiesAccepted
from cookies.models import CookiesConsents, CookieSettings


def cookies_check(request):
    session_key = request.session.session_key
    if CookiesConsents.objects.filter(session_id=session_key).exists():
        cookies = get_object_or_404(CookiesConsents, session_id=session_key)
        try:
            cookies_setting = get_object_or_404(CookieSettings, pk=1)
        except Exception as e:
            cookies_setting = None
        form = AllCookiesAccepted(instance=cookies)
        return {
            "cookies": cookies,
            "form": form,
            "cookies_setting": cookies_setting,
        }
    else:
        try:
            cookies_setting = get_object_or_404(CookieSettings, pk=1)
        except Exception as e:
            cookies_setting = None
        form = AllCookiesAccepted(request.GET)
        return {
            "form": form,
            "cookies_setting": cookies_setting,
        }
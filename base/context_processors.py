from django.shortcuts import get_object_or_404

from cookies.forms import AllCookiesAccepted
from cookies.models import CookiesConsents, CookieSettings


def cookies_check(request):
    session_key = request.session.session_key
    if CookiesConsents.objects.filter(session_id=session_key).exists():
        cookies = get_object_or_404(CookiesConsents, session_id=session_key)
        cookies_setting = get_object_or_404(CookieSettings, pk=1)
        form = AllCookiesAccepted(instance=cookies)
        return {
            "cookies": cookies,
            "form": form,
            "cookies_setting": cookies_setting,
        }
    else:
        form = AllCookiesAccepted(request.GET)
        return {
            "form": form,
            "cookies_setting": cookies_setting,
        }
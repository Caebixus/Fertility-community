from django.shortcuts import get_object_or_404

from cookies.forms import AllCookiesAccepted
from cookies.models import CookiesConsents


def cookies_check(request):
    # ip_address = "10.10.50.10"
    session_key = request.session.session_key
    if CookiesConsents.objects.filter(session_id=session_key).exists():
        cookies = get_object_or_404(CookiesConsents, session_id=session_key)
        form = AllCookiesAccepted(instance=cookies)
        return {
            "cookies": cookies,
            "form": form,
        }
    else:
        form = AllCookiesAccepted(request.GET)
        return {
            "form": form,
        }
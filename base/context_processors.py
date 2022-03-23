from django.shortcuts import get_object_or_404
from cookies.forms import AllCookiesAccepted
from cookies.models import CookiesConsents, CookieSettings
from owners.models import AuthenticatedUser


def authentication_clinic_coach(request):
    user = request.user
    if user.id != None:
        auth_user = AuthenticatedUser.objects.get(user__id=user.pk)
        return {
            "auth_user": auth_user,
        }
    else:
        return {
            "auth_user": False,
        }


def cookies_check(request):
    session_key = request.session.session_key
    cookies_list = request.COOKIES
    cookies_setting = get_object_or_404(CookieSettings, pk=1)

    if 'cookie_variable' in cookies_list:
        cookie_variable = request.COOKIES['cookie_variable']
        if CookiesConsents.objects.filter(custom_cookie=cookie_variable).exists():
            cookies = get_object_or_404(CookiesConsents, custom_cookie=cookie_variable)
            formupdate = AllCookiesAccepted(instance=cookies)
            return {
                "cookies": cookies,
                "formupdate": formupdate,
                "cookies_setting": cookies_setting,
            }
        else:
            formNew = AllCookiesAccepted(request.GET)
            return {
                "formNew": formNew,
                "cookies_setting": cookies_setting,
            }

    else:
        if CookiesConsents.objects.filter(session_id=session_key).exists():
            cookies = get_object_or_404(CookiesConsents, session_id=session_key)
            formupdate = AllCookiesAccepted(instance=cookies)
            return {
                "cookies": cookies,
                "formupdate": formupdate,
                "cookies_setting": cookies_setting,
            }

        else:
            formNew = AllCookiesAccepted(request.GET)
            return {
                "formNew": formNew,
                "cookies_setting": cookies_setting,
            }
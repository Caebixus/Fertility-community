from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import AllCookiesAccepted
from .models import CookiesConsents


def cookies(request):
    # Je potřeba zrefaktorovat if & else větve na fce

    redirect_to = request.META.get("HTTP_REFERER")
    date = datetime.now()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[-1].strip()
    else:
        ip_address = request.META.get('REMOTE_ADDR')

    cookies_list = request.COOKIES
    if 'cookie_variable' in cookies_list:
        cookie_variable = request.COOKIES['cookie_variable']

        if request.method == "POST" and "all_cookies_accepted" in request.POST:
            if CookiesConsents.objects.filter(custom_cookie=cookie_variable).exists():
                cookies = CookiesConsents.objects.get(custom_cookie=cookie_variable)
                form = AllCookiesAccepted(request.POST, instance=cookies)
                if form.is_valid() and cookie_variable is not None:
                    form = form.save(commit=False)
                    form.consent_created = date
                    form.ip_address = ip_address
                    form.save()
                    return HttpResponseRedirect(redirect_to)
                else:
                    pass

            else:
                form = AllCookiesAccepted(request.POST)
                if form.is_valid() and cookie_variable is not None:
                    form = form.save(commit=False)
                    form.consent_created = date
                    form.ip_address = ip_address
                    form.custom_cookie = cookie_variable
                    form.marketing_cookies = True
                    form.analytical_cookies = True
                    form.save()
                    return HttpResponseRedirect(redirect_to)
                else:
                    pass

        elif request.method == "POST" and "cookies_changed" in request.POST:
            if CookiesConsents.objects.filter(custom_cookie=cookie_variable).exists():
                cookies = CookiesConsents.objects.get(custom_cookie=cookie_variable)
                form = AllCookiesAccepted(request.POST, instance=cookies)
                if form.is_valid() and cookie_variable is not None:
                    form = form.save(commit=False)
                    form.consent_created = date
                    form.ip_address = ip_address
                    form.save()
                    return HttpResponseRedirect(redirect_to)
                else:
                    pass
            else:
                form = AllCookiesAccepted(request.POST)
                if form.is_valid() and cookie_variable is not None:
                    form = form.save(commit=False)
                    form.ip_address = ip_address
                    form.custom_cookie = cookie_variable
                    form.consent_created = date
                    form.save()
                    return HttpResponseRedirect(redirect_to)
                else:
                    pass

        elif request.method == "POST" and "cookies_changed_update" in request.POST:
            cookies = CookiesConsents.objects.get(custom_cookie=cookie_variable)
            form = AllCookiesAccepted(request.POST, instance=cookies)
            if form.is_valid() and cookie_variable is not None:
                form = form.save(commit=False)
                form.consent_created = date
                form.ip_address = ip_address
                form.save()
                return HttpResponseRedirect(redirect_to)
            else:
                pass
        return redirect(redirect_to)

    else:
        return redirect(redirect_to)

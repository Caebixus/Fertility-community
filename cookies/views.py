from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import AllCookiesAccepted
from .models import CookiesConsents


def cookies(request):
    redirect_to = request.META.get("HTTP_REFERER", "/")
    date = datetime.now()

    # ip_address = "10.10.50.10" (pro testování)
    # ip_address = request.META.get('REMOTE_ADDR')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[-1].strip()
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    if request.method == "POST" and "all_cookies_accepted" in request.POST:
        if CookiesConsents.objects.filter(session_id=session_key).exists():
            cookies = CookiesConsents.objects.get(session_id=session_key)
            form = AllCookiesAccepted(request.POST, instance=cookies)
            if form.is_valid() and session_key is not None:
                form = form.save(commit=False)
                form.consent_created = date
                form.ip_address = ip_address
                form.save()
                return HttpResponseRedirect(redirect_to)
            else:
                pass

        else:
            form = AllCookiesAccepted(request.POST)
            if form.is_valid() and session_key is not None:
                form = form.save(commit=False)
                form.consent_created = date
                form.ip_address = ip_address
                form.session_id = session_key
                form.marketing_cookies = True
                form.analytical_cookies = True
                form.save()
                return HttpResponseRedirect(redirect_to)
            else:
                pass

    elif request.method == "POST" and "cookies_changed" in request.POST:
        if CookiesConsents.objects.filter(session_id=session_key).exists():
            cookies = CookiesConsents.objects.get(session_id=session_key)
            form = AllCookiesAccepted(request.POST, instance=cookies)
            if form.is_valid() and session_key is not None:
                form = form.save(commit=False)
                form.consent_created = date
                form.ip_address = ip_address
                form.save()
                return HttpResponseRedirect(redirect_to)
            else:
                pass
        else:
            form = AllCookiesAccepted(request.POST)
            if form.is_valid() and session_key is not None:
                form = form.save(commit=False)
                form.ip_address = ip_address
                form.session_id = session_key
                form.consent_created = date
                form.save()
                return HttpResponseRedirect(redirect_to)
            else:
                pass

    elif request.method == "POST" and "cookies_changed_update" in request.POST:
        cookies = CookiesConsents.objects.get(session_id=session_key)
        form = AllCookiesAccepted(request.POST, instance=cookies)
        if form.is_valid() and session_key is not None:
            form = form.save(commit=False)
            form.consent_created = date
            form.ip_address = ip_address
            form.save()
            return HttpResponseRedirect(redirect_to)
        else:
            pass
    return redirect("/")

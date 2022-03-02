from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages, auth
from django.contrib.auth.models import User

from blog.models import Blog
from .models import AuthenticatedUser
from django.core.mail import send_mail
from .functions import get_random_string
from coaches.models import Coaches, SnippetNew, PreferredLanguage
from .forms import CreateNewCoachForm
from coaches.forms import UpdateCoachForm


def register_as_coach(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if passwords match
        if password == password2:
            #check Email
            if User.objects.filter(email=email).exists():
                messages.error(request, '- That email is already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=password, username=username)
                #login after registered
                auth.login(request, user)

                random_auth_number = get_random_string(10)
                print(random_auth_number)

                auth_user = request.user

                authenticateduser = AuthenticatedUser()
                authenticateduser.user = auth_user
                authenticateduser.register_as_coach = True

                authenticateduser.random_auth_string = random_auth_number
                authenticateduser.save()

                send_mail(
                    "Confirm registration - fertilitycommunity.com",
                    "Hello,\n" +
                    "Please activate your new account. Copy code below into a field in your account dashboard:\n" +
                    "\n" +
                    str(random_auth_number) +
                    "\n" +
                    "\nFertilityCommunity team\n" +
                    "This is an automated message, please do not reply",
                    "info@fertilitycommunity.com",
                    [user.email],
                    fail_silently=False,
                )
                return redirect('notActiveUser')

        else:
            messages.error(request, '- Passwords do not match')
            return redirect('register-as-coach')
    else:
        return render(request, 'owners/coach/signup-as-coach.html')


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def coach_dashboard(request):
    user = request.user
    authenticated = AuthenticatedUser.objects.filter(pk=user.pk)

    try:
        if user.authenticateduser.is_activated == False:
            return redirect('notActiveUser')
        else:
            if Coaches.objects.filter(coach_user=user).exists():
                coaches = Coaches.objects.get(coach_user=user)
                snippets = SnippetNew.objects.filter(snippet_owner=coaches)
                print(snippets)

                count_free_blogs = Blog.objects.filter(snippet_blog_conn__isnull=True).count()

                blogs = Blog.objects.all().order_by('-created_at')

                for blog in blogs:
                    if blog.snippet_blog_conn.filter(snippet_blog_relationship__in=blogs).exists():
                        snippet = blog.snippet_blog_conn.filter(snippet_blog_relationship_id=blog.id)
                        count = blog.snippet_blog_conn.filter(snippet_blog_relationship_id=blog.id).count()

                        context = {
                            'authenticated': authenticated,
                            'coaches': coaches,
                            'snippets': snippets,
                            'count_free_blogs': count_free_blogs,
                            'snippet': snippet,
                            'count': count,
                            'blogs': blogs,
                        }

                return render(request, 'owners/coach/coach-dashboard.html', context)

            else:
                context = {
                    'authenticated': authenticated,
                    'no_model': 'no_model',
                }

                return render(request, 'owners/coach/coach-dashboard.html', context)

    except ObjectDoesNotExist:
        return redirect('notActiveUser')


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def create_coach_profile(request):
    user = request.user
    form = CreateNewCoachForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form.save_m2m()

        # send_mail(
        #     'Coach profile vytvořen -' + str(form.coach_user),
        #     'Právě někdo vytvořil nový coach profile a je třeba jej ověřit ' +
        #     '\nUser username: ' + str(user.email),
        #     'info@fertilitycommunity.com',
        #     ['David.langr@fertilitycommunity.com'],
        #     fail_silently=False,
        #     )

        messages.success(request, '- Coach profile successfully created. Wait for our team to review and publish it.')
        return redirect('coach_dashboard')

    context = {
        'form': form,
    }

    return render(request, 'owners/coach/create-coach.html', context)


class UpdateNewCoachForm:
    pass


@login_required(login_url='https://www.fertilitycommunity.com/account/signup-as-coach')
def update_coach_profile(request, coaches_id):
    user = request.user
    instance = get_object_or_404(Coaches, pk=coaches_id)
    print(instance)
    form = UpdateCoachForm(user, request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.coach_updated = datetime.now()
        obj.coach_user = user
        obj.save()
        list_of_languages = form.cleaned_data['coach_preferred_languages']
        form._save_m2m()

        # print(list_of_languages)
        # defaults = {'coach_preferred_languages': list_of_languages}
        # PreferredLanguage.objects.update_or_create(coaches_relationship=coaches_id, preferred_language__in=list_of_languages, defaults={'coaches_relationship': coaches_id, 'preferred_language': list_of_languages})

        # send_mail(
        #     'Coach profile upraven -' + str(form.coach_user),
        #     'Právě někdo upravil svůj profile a je třeba jej ověřit ' +
        #     '\nUser username: ' + str(user.email),
        #     'info@fertilitycommunity.com',
        #     ['David.langr@fertilitycommunity.com'],
        #     fail_silently=False,
        #     )

        messages.success(request, '- Coach profile successfully updated. Wait for our team to review and publish it.')
        return redirect('coach_dashboard')

    context = {
        'form': form,
    }

    return render(request, 'owners/coach/update-coach.html', context)
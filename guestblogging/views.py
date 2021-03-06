from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages, auth
from django.conf import settings
from django.contrib.auth.models import User
from clinic.models import BasicClinic
from django.utils import timezone
from datetime import datetime, timedelta
from contact.forms import ContactForm, ClaimForm
from django.core.mail import send_mail
from django.forms.fields import Field, FileField
from .models import GuestAuthor, GuestBlog
from .choices import GUEST_BLOG_TAG_CHOICES
from .forms import CreateGuestAuthor, CreateGuestBlog


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def guestblogging(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id)
    author = GuestAuthor.objects.filter(guestauthor_id=listing_id)
    blog = GuestBlog.objects.filter(guestblogauthor_id__in=author)



    context = {
        'instance': instance,
        'author': author,
        'blog': blog,
    }

    return render(request, 'owners/guest-blogging/guest-blogging.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create_guest_author(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id)
    form = CreateGuestAuthor(request.POST or None, request.FILES or None, initial={'guestauthor': instance.id})

    klinika = instance.clinicName

    listing = GuestAuthor.objects.all()
    listing = listing.filter(guestauthor__id=listing_id)
    count = listing.count()

    if instance.pro_is_published == True:
        authorNumber = 1
    elif instance.ppq_is_published == True:
        authorNumber = 5
    else:
        authorNumber = 0

    if count < authorNumber:
        if form.is_valid():
            form = form.save(commit=False)
            form.guestauthor = instance
            form.save()

            instance.guestAuthorCounterNumber += int(1)
            instance.save()

            send_mail(
                'New guest author created',
                'Právě někdo vytvořil nového guest authora ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )

            context = {
                'instance': instance,
                'form': form,
                'authorNumber': authorNumber,
            }

            messages.success(request, '- author successfully created')
            return redirect('guestblogging', listing_id=instance.id)

        context = {
            'instance': instance,
            'form': form,
            'authorNumber': authorNumber,
        }

    else:
        messages.warning(request, '- the maximum number of guest author for this clinic paid plan is {} ' .format(authorNumber))
        return redirect('guestblogging', listing_id=instance.id)

    context = {
        'instance': instance,
        'form': form,
        'authorNumber': authorNumber,
    }

    return render(request, 'owners/guest-blogging/create-guest-author.html', context)


@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def create_guest_blog(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id)
    author = GuestAuthor.objects.filter(guestauthor__id=listing_id)
    form = CreateGuestBlog(request.POST or None, request.FILES or None)
    form.fields['guestblogauthor'].queryset = GuestAuthor.objects.filter(guestauthor__id=listing_id)

    klinika = instance.clinicName


    listing = GuestBlog.objects.all()
    listing = listing.filter(guestblogauthor__guestauthor__id=instance.id)
    count = listing.count()

    if instance.pro_is_published == True:
        blogNumber = 1
    elif instance.ppq_is_published == True:
        blogNumber = 5
    else:
        blogNumber = 0

    if count < blogNumber:
        if form.is_valid():
            form = form.save(commit=False)
            form.guestblogcreatedat = datetime.now()
            form.save()

            instance.guestBlogCounterNumber += int(1)
            instance.save()

            send_mail(
                'New guest blog post created',
                'Právě někdo vytvořil nového guest blog post ' +
                '\nClinic username: ' + str(klinika),
                'info@fertilitycommunity.com',
                ['David.langr@fertilitycommunity.com'],
                fail_silently=False,
                )

            context = {
                'instance': instance,
                'form': form,
                'blogNumber': blogNumber,
                'count': count,
            }

            messages.success(request, '- blogpost successfully created & sent to review')
            return redirect('guestblogging', listing_id=instance.id)

        context = {
            'instance': instance,
            'form': form,
            'blogNumber': blogNumber,
            'count': count,
        }

    else:
        messages.warning(request, '- the maximum number of guest blog posts for this clinic paid plan is {} ' .format(blogNumber))
        return redirect('guestblogging', listing_id=instance.id)


    context = {
        'instance': instance,
        'form': form,
        'blogNumber': blogNumber,
        'count': count,
    }

    return render(request, 'owners/guest-blogging/create-guest-blog.html', context)

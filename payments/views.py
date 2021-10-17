from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from clinic.models import BasicClinic
from .models import Customer
from packages.models import Package
from guestblogging.models import GuestBlog
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .choices import CATEGORY_CHOICES_ISO
import stripe

stripe.api_key = settings.STRIPE_PRIVATE_KEY
stripePublickKey = settings.STRIPE_PUBLIC_KEY
stripeWebhookPrivateKey = settings.STRIPE_WEBHOOK_PRIVATE_KEY

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def billinginfo(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    try:
        existingCustomer = Customer.objects.get(customerClinic_id=listing_id)
    except Customer.DoesNotExist:
        existingCustomer = None

    if existingCustomer == None:
        if request.method == 'GET':
            context = {'instance': instance, 'CATEGORY_CHOICES_ISO': CATEGORY_CHOICES_ISO, }
            return render(request, 'owners/payments/billinginfo.html', context)
        else:
            stripe_customer = stripe.Customer.create(
                    name=instance.clinicName,
                    email=instance.contact_email,
                    address={
                        'line1': request.POST['billingsAddressLine1'],
                        'city': request.POST['billingsAddressCity'],
                        'country': request.POST['billingsAddressCountry'],
                        'postal_code': request.POST['billingsAddressZipPostal'],
                        'state': request.POST['billingsAddressState'],
                    },
                )

            customer = Customer()
            customer.customerClinic = instance
            customer.stripeid = stripe_customer.id
            customer.save()

            send_mail(
                'Customer created',
                'Someone created clinic as customer ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )

            #Pro-Btn-monthly
            session1 = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1J2wXxEHpkY9RbxJ0cGbdiMS',
                    'quantity': 1,
                }],
                customer=customer.stripeid,
                mode='subscription',
                success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id1={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('dashboard')),
            )

            #Pro-Btn-yearly
            session2 = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1J2wY2EHpkY9RbxJSYYqge4l',
                    'quantity': 1,
                }],
                customer=customer.stripeid,
                mode='subscription',
                success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id2={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('dashboard')),
            )

            context = {
                'instance': instance,
                'customer': customer,
                'session_id1': session1.id,
                'session_id2': session2.id,
                'stripe_public_key': stripePublickKey,
            }

            return render(request, 'owners/payments/checkout.html', context)

    else:
        messages.error(request, 'Already customer, for managing subscriptions go to the customer portal')
        return redirect('dashboard')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def billinginfo1(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)

    try:
        existingCustomer = Customer.objects.get(customerClinic_id=listing_id)
    except Customer.DoesNotExist:
        existingCustomer = None

    if existingCustomer == None:
        if request.method == 'GET':
            context = {'instance': instance, 'CATEGORY_CHOICES_ISO': CATEGORY_CHOICES_ISO, }
            return render(request, 'owners/payments/billinginfo1.html', context)
        else:
            stripe_customer = stripe.Customer.create(
                    name=instance.clinicName,
                    email=instance.contact_email,
                    address={
                        'line1': request.POST['billingsAddressLine1'],
                        'city': request.POST['billingsAddressCity'],
                        'country': request.POST['billingsAddressCountry'],
                        'postal_code': request.POST['billingsAddressZipPostal'],
                        'state': request.POST['billingsAddressState'],
                    },
                )

            customer = Customer()
            customer.customerClinic = instance
            customer.stripeid = stripe_customer.id
            customer.save()

            #Premium-Btn-monthly
            session3= stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1HZetuEHpkY9RbxJyRjQvzGe',
                    'quantity': 1,
                }],
                customer=customer.stripeid,
                mode='subscription',
                success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id3={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('dashboard')),
            )

            #Premium-Btn-yearly
            session4 = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price': 'price_1HZetuEHpkY9RbxJs17Cfx5h',
                    'quantity': 1,
                }],
                customer=customer.stripeid,
                mode='subscription',
                success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id4={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('dashboard')),
            )

            context = {
                'instance': instance,
                'customer': customer,
                'session_id3': session3.id,
                'session_id4': session4.id,
                'stripe_public_key': stripePublickKey,
            }

            return render(request, 'owners/payments/checkout1.html', context)

    else:
        messages.error(request, 'Already customer, for managing subscriptions go to the customer portal')
        return redirect('dashboard')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def payments(request, listing_id):
    instance = get_object_or_404(BasicClinic, pk=listing_id, clinicOwner_id=request.user)
    customer = get_object_or_404(Customer, customerClinic_id=instance)

    if request.method == 'POST':
        customer_portal = stripe.billing_portal.Session.create(
            customer=customer.stripeid,
            return_url='https://www.fertilitycommunity.com/account/dashboard',
        )

        return redirect(customer_portal.url)

    context = {
        'instance': instance,
        'customer': customer,
    }

    return render(request, 'owners/payments/payments.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def successpay(request):
    return render(request, 'owners/payments/successpay.html')

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def checkout(request, pk):
    instance = get_object_or_404(BasicClinic, pk=pk, clinicOwner_id=request.user)
    customer = get_object_or_404(Customer, customerClinic_id=instance)

    #Pro-Btn-monthly
    session1 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1J2wXxEHpkY9RbxJ0cGbdiMS',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id1={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )

    #Pro-Btn-yearly
    session2 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1J2wY2EHpkY9RbxJSYYqge4l',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id2={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )

    context = {
        'instance': instance,
        'customer': customer,
        'session_id1': session1.id,
        'session_id2': session2.id,
        'stripe_public_key': stripePublickKey,
    }

    return render(request, 'owners/payments/checkout.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def checkout1(request, pk):
    instance = get_object_or_404(BasicClinic, pk=pk, clinicOwner_id=request.user)
    customer = get_object_or_404(Customer, customerClinic_id=instance)
    #Premium-Btn-monthly
    session3 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HZetuEHpkY9RbxJyRjQvzGe',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id3={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )
    #Premium-Btn-yearly
    session4 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HZetuEHpkY9RbxJs17Cfx5h',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id4={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )

    context = {
        'instance': instance,
        'customer': customer,
        'session_id3': session3.id,
        'session_id4': session4.id,
        'stripe_public_key': stripePublickKey,
    }

    return render(request, 'owners/payments/checkout1.html', context)

@login_required(login_url='https://www.fertilitycommunity.com/account/signin')
def checkout2(request, pk):
    instance = get_object_or_404(BasicClinic, pk=pk, clinicOwner_id=request.user)
    customer = get_object_or_404(Customer, customerClinic_id=instance)
    #Pro-Btn-yearly
    session1 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1J2wY2EHpkY9RbxJSYYqge4l',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id1={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )
    #Pro-Btn-monthly
    session2 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1J2wXxEHpkY9RbxJ0cGbdiMS',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id2={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )
    #Premium-Btn-monthly
    session3 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HZetuEHpkY9RbxJyRjQvzGe',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id3={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )
    #Premium-Btn-yearly
    session4 = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HZetuEHpkY9RbxJs17Cfx5h',
            'quantity': 1,
        }],
        customer=customer.stripeid,
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('successpay')) + '?session_id4={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('dashboard')),
    )

    context = {
        'instance': instance,
        'customer': customer,
        'session_id1': session1.id,
        'session_id2': session2.id,
        'session_id3': session3.id,
        'session_id4': session4.id,
        'stripe_public_key': stripePublickKey,
    }

    return render(request, 'owners/payments/checkout2.html', context)

@csrf_exempt
def stripe_webhook(request):

    # You can find your endpoint's secret in your webhook settings
    endpoint_secret = stripeWebhookPrivateKey

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        line_items = stripe.checkout.Session.list_line_items(session['id'], limit=1)
        customer = get_object_or_404(Customer, stripeid=session.customer)
        customer.stripe_subscription_id = session.subscription
        customer.membership = True
        customer.save()
        instance = get_object_or_404(BasicClinic, pk=customer.customerClinic.id)
        send_mail(
            'Customer created',
            'Someone created clinic as customer ' +
            '\nClinic username: ' + str(customer.customerClinic),
            'info@fertilitycommunity.com',
            ['info@fertilitycommunity.com'],
            fail_silently=False,
            )

        # Create a new subscription and mark it as paid this month.
        # subscription = sign_up_customer(customer_email, subscription_id)

    if event['type'] == 'customer.deleted':
        session = event['data']['object']
        customer = get_object_or_404(Customer, stripeid=session.id)
        customer.delete()
        instance = get_object_or_404(BasicClinic, pk=customer.customerClinic.id)
        instance.ppq_is_published = False
        instance.pro_is_published = False
        instance.save()

        package = Package.objects.filter(packageclinic_id=instance)
        Package.objects.filter(id__in=package).update(is_package_active=False)

        guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id)
        GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=False)

        send_mail(
            'Customer lost',
            'Someone deleted customer ' +
            '\nClinic username: ' + str(customer.customerClinic),
            'info@fertilitycommunity.com',
            ['info@fertilitycommunity.com'],
            fail_silently=False,
            )

    if event['type'] == 'customer.subscription.created':
        pass

    if event['type'] == 'payment_intent.succeeded':
        pass

    if event['type'] == 'invoice.paid':
        session = event['data']['object']
        customer = get_object_or_404(Customer, stripeid=session.customer)
        customer.membership = True
        customer.save()
        send_mail(
            'Subscription invoice paid',
            'Someone subscribed and paid invoice ' +
            '\nClinic username: ' + str(customer.customerClinic),
            'info@fertilitycommunity.com',
            ['info@fertilitycommunity.com'],
            fail_silently=False,
            )

    if event['type'] == 'customer.subscription.deleted':
        session = event['data']['object']
        customer = get_object_or_404(Customer, stripe_subscription_id=session.id)
        customer.membership = False
        customer.stripe_subscription_id = None
        customer.save()
        instance = get_object_or_404(BasicClinic, pk=customer.customerClinic.id)
        sessionPlan = session.plan.id
        if sessionPlan == 'price_1HZetuEHpkY9RbxJyRjQvzGe' or sessionPlan == 'price_1HZetuEHpkY9RbxJs17Cfx5h': #PREMIUM Plans
            instance.ppq_is_published = False
            instance.pro_is_published = False
            instance.save()

            package = Package.objects.filter(packageclinic_id=instance)
            Package.objects.filter(id__in=package).update(is_package_active=False)

            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id)
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=False)

            send_mail(
                'Subscription deleted',
                'Someone unsubscribed ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
        else:
            instance.ppq_is_published = False
            instance.pro_is_published = False
            instance.save()
            package = Package.objects.filter(packageclinic_id=instance)
            Package.objects.filter(id__in=package).update(is_package_active=False)
            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id)
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=False)
            send_mail(
                'Subscription deleted',
                'Someone unsubscribed ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )

    if event['type'] == 'customer.subscription.updated':
        session = event['data']['object']
        lines = stripe.Subscription.list(limit=3)
        planid = lines.data[-1]
        planidplan = planid.plan.id
        customer = get_object_or_404(Customer, stripeid=session.customer)
        instance = get_object_or_404(BasicClinic, pk=customer.customerClinic.id)
        if planidplan == 'price_1HZetuEHpkY9RbxJyRjQvzGe' or planidplan == 'price_1HZetuEHpkY9RbxJs17Cfx5h': #PREMIUM Plans
            instance.ppq_is_published = True
            instance.pro_is_published = False
            instance.save()

            package = Package.objects.filter(packageclinic_id=instance).order_by('pk')[0:6]
            Package.objects.filter(id__in=package).update(is_package_active=True)
            packageFalse = Package.objects.filter(packageclinic_id=instance).order_by('pk')[6:]
            Package.objects.filter(id__in=packageFalse).update(is_package_active=False)

            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id).order_by('pk')[0:5]
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=True)

            customer.membership = True
            send_mail(
                'Subscription updated',
                'Someone updated subscription ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
        elif planidplan == 'price_1J2wXxEHpkY9RbxJ0cGbdiMS' or planidplan == 'price_1J2wY2EHpkY9RbxJSYYqge4l': #PRO Plans
            instance.ppq_is_published = False
            instance.pro_is_published = True
            instance.save()

            package = Package.objects.filter(packageclinic_id=instance).order_by('pk')[0:2]
            Package.objects.filter(id__in=package).update(is_package_active=True)
            packageFalse = Package.objects.filter(packageclinic_id=instance).order_by('pk')[2:]
            Package.objects.filter(id__in=packageFalse).update(is_package_active=False)

            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id).order_by('pk')[0:1]
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=True)
            guestblogFalse = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id).order_by('pk')[1:]
            GuestBlog.objects.filter(id__in=guestblogFalse).update(guestblogactive=False)

            customer.membership = True
            send_mail(
                'Subscription updated',
                'Someone updated subscription ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
        else:
            customer.membership = False
            send_mail(
                'Subscription lost',
                'Someone unsubscribed ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
        customer.save()


    if event['type'] == 'invoice.payment_failed':
        session = event['data']['object']
        customer = get_object_or_404(Customer, stripeid=session.id)
        customer.membership = False
        customer.save()
        instance = get_object_or_404(BasicClinic, pk=customer.customerClinic.id)
        sessionPlan = session.plan.id
        if sessionPlan == 'price_1HZetuEHpkY9RbxJyRjQvzGe' or sessionPlan == 'price_1HZetuEHpkY9RbxJs17Cfx5h': #PREMIUM Plans
            instance.ppq_is_published = False
            instance.pro_is_published = False
            instance.save()
            package = Package.objects.filter(packageclinic_id=instance)
            Package.objects.filter(id__in=package).update(is_package_active=False)
            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id)
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=False)
            send_mail(
                'Subscription invoice failed',
                'Someone unsubscribed ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )
        else:
            instance.ppq_is_published = False
            instance.pro_is_published = False
            instance.save()
            package = Package.objects.filter(packageclinic_id=instance)
            Package.objects.filter(id__in=package).update(is_package_active=False)
            guestblog = GuestBlog.objects.filter(guestblogauthor__guestauthor__id=instance.id)
            GuestBlog.objects.filter(id__in=guestblog).update(guestblogactive=False)
            send_mail(
                'Subscription invoice failed',
                'Someone unsubscribed ' +
                '\nClinic username: ' + str(customer.customerClinic),
                'info@fertilitycommunity.com',
                ['info@fertilitycommunity.com'],
                fail_silently=False,
                )

    if event['Type'] == 'subscription_schedule.canceled':
        session = event['data']['object']
        customer = get_object_or_404(Customer, stripeid=session.id)

        send_mail(
            'Subscription canceled',
            'Someone just now canceled subscription on stripe' +
            '\nClinic username: ' + str(customer.customerClinic),
            'info@fertilitycommunity.com',
            ['info@fertilitycommunity.com'],
            fail_silently=False,
        )

    return HttpResponse(status=200)

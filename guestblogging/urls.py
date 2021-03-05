from django.urls import path

from . import views

urlpatterns = [
    path('guest-blogging/<int:listing_id>', views.guestblogging, name='guestblogging'),

    path('guest-blogging/create-guest-author/<int:listing_id>', views.create_guest_author, name='create_guest_author'),
    path('guest-blogging/create-guest-blog/<int:listing_id>', views.create_guest_blog, name='create_guest_blog'),
]

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fertility.settings')
django.setup()

from owners.models import AuthenticatedUser

auth_user = AuthenticatedUser.objects.all()

for user in auth_user:
    user.register_as_clinic = True
    user.register_as_coach = True
    user.save()
from django.contrib.auth.models import User
from django.db import models

class ownerProInterested(models.Model):
    clinicOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_interested = models.BooleanField(default=False)

    def __str__(self):
        return str(self.clinicOwner)

class ProUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paidPropublished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class AuthenticatedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_activated = models.BooleanField(default=False)
    random_auth_string = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.user)



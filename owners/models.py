from django.contrib.auth.models import User
from clinic.models import BasicClinic
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

class SingleClinicBestArticleText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Best world clinics text
    clinic_world = models.OneToOneField(BasicClinic, on_delete=models.CASCADE, null=True, blank=True)
    best_clinic_world_text = models.TextField(max_length=1000, blank=True, null = True)
    best_clinic_world_activated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.clinic_world)
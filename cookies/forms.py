from django import forms

from .models import CookiesConsents


class AllCookiesAccepted(forms.ModelForm):
    ip_address = forms.CharField(label="IP adresa", max_length=100, required=False)
    analytical_cookies = forms.BooleanField(label="Analytické cookies", required=False)
    marketing_cookies = forms.BooleanField(label="Marketingové cookies", required=False)
    consent_created = forms.DateTimeField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = CookiesConsents
        fields = [
            "ip_address",
            "analytical_cookies",
            "marketing_cookies",
            "consent_created",
        ]

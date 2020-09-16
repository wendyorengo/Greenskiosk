from django import forms
from .models import Kiosk, KioskOwner


class KioskForm(forms.ModelForm):
    class Meta:
        model = Kiosk
        fields = '__all__'

class KioskownerForm(forms.ModelForm):
    class Meta:
        model = KioskOwner
        fields = "__all__"


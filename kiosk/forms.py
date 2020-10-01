from django import forms
from .models import Kiosk


class KioskForm(forms.ModelForm):
    class Meta:
        model = Kiosk
        fields = '__all__'

        fields = ["owner", "name", "date_opened", "street_address", "currency", "phone_number", "business_type"]

        widgets = {
            'owner' :forms.TextInput(attrs={'class':'form-control'}),
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'date_opened' :forms.TextInput(attrs={'class':'form-control'}),
            'street_address' :forms.TextInput(attrs={'class':'form-control'}),
            'currency' :forms.TextInput(attrs={'class':'form-control'}),
            'phone_number' :forms.TextInput(attrs={'class':'form-control'}),
            'business_type' :forms.TextInput(attrs={'class':'form-control'}),
            
        }



        

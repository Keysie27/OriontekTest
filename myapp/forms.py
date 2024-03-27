from django import forms
from .models import Client, Address

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email']

class AddressForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label="Cliente")

    class Meta:
        model = Address
        fields = ['client', 'street', 'city', 'postal_code']


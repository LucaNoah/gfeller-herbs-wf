from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('email_address', 'full_name', 'delivery_address1', 'delivery_address2', 'zip_code', 'state', 'country',)
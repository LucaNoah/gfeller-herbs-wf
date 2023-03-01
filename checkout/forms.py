from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "email_address",
            "phone_number",
            "full_name",
            "delivery_address",
            "town_or_city",
            "zip_code",
            "state",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add classes to all fields
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'checkout-style-input'

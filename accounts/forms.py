from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add classes to all fields
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = False

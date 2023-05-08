from django import forms
from .models import UserAccount, CustomerFeedback, Return


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
            self.fields["has_newsletter_sub"].label = "Chek to Subscribe"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = "__all__"


class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = "__all__"

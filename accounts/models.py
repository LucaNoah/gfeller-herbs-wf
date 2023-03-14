from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_delivery_address = models.CharField(
        max_length=100, null=True, blank=True
    )
    default_town_or_city = models.CharField(
        max_length=80, null=True, blank=True
    )
    default_zip_code = models.CharField(max_length=20, null=True, blank=True)
    default_state = models.CharField(max_length=100, null=True, blank=True)
    default_country = CountryField(
        blank_label="Select...", null=True, blank=True
    )
    has_newsletter_sub = models.BooleanField(
        default=False
    )
    newsletter_email_address = models.EmailField(
        max_length=75, null=True, blank=True
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    """
    Create or update user account
    """
    if created:
        UserAccount.objects.create(user=instance)
    instance.useraccount.save()


class CustomerFeedback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer_feedback"
    )
    PRODUCTS = "Products/Product Range"
    CHECKOUT = "Order/Payment"
    STORE = "Store Structure/Design"
    GENERAL = "General Improvement Suggestions"
    OTHER = "Other"
    REASON_CHOICES = [
        (PRODUCTS, "Products/Product Range"),
        (CHECKOUT, "Order/Payment"),
        (STORE, "Store Structure/Design"),
        (GENERAL, "General Improvement Suggestions"),
        (OTHER, "Other"),
    ]
    reason = models.CharField(
        max_length=31,
        choices=REASON_CHOICES,
        default=GENERAL,
    )
    content = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

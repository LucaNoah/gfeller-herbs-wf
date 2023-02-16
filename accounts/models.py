from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    """
    User account model to store delivery information and an order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_delivery_address = models.CharField(max_length=100, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=80, null=True, blank=True)
    default_zip_code = models.CharField(max_length=20, null=True, blank=True)
    default_state = models.CharField(max_length=100, null=True, blank=True)
    default_country = CountryField(blank_label='Select...', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    """
    Create or update user account
    """
    if created:
        UserAccount.objects.create(user=instance)
    instance.userprofile.save()

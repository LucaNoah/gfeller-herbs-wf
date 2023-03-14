import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from accounts.models import UserAccount


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, null=False, blank=False, editable=False
    )
    user_account = models.ForeignKey(
        UserAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, null=False, blank=False
    )
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False, blank=False
    )
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, null=False, blank=False
    )
    email_address = models.EmailField(max_length=75, null=False, blank=False)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    delivery_address = models.CharField(
        max_length=100, null=False, blank=False
    )
    town_or_city = models.CharField(
        max_length=80, null=False, blank=False, default=""
    )
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label="Select...", null=False, blank=False)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.order_total = (
            self.orderlineitems.aggregate(Sum("lineitem_total"))[
                "lineitem_total__sum"
            ]
            or 0
        )
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override original save method to set an order number if
        none has been set yet
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="orderlineitems",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=False, blank=False
    )
    quantity = models.IntegerField(default=0, null=False, blank=False)
    product_weight = models.CharField(
        max_length=5, null=True, blank=True
    )  # 100g, 250g, 500g, (1000g)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override original save method to set the lineitem total and
        update oder total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"SKU: in order {self.order.order_number}"

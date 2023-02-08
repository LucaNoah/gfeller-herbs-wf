import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=20, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False, blank=False)
    email_address = models.EmailField(max_length=75, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    delivery_address1 = models.CharField(max_length=100, null=False, blank=False)
    delivery_address2 = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.DecimalField(max_digits=20, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=80, null=True, blank=False)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, related_name=orderlineitems on_delete=models.CASCADE, null=False, blank= False)
    product = models.ForeignKey(Product, on_delete=CASCADE, null=False, blank=False)
    quantity = models.IntegerField(max_length=3, default=0, null=False, blank=False)
    product_weight = models.CharField(max_length=5, null=True, blank=True) # 100g, 250g, 500g, (1000g)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


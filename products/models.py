from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=250)
    description = models.TextField(blank=False, null=False)
    on_sale = models.BooleanField(default=False)
    old_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=True, blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=13, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True, max_length=1024)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(
        "Product", null=False, blank=False, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_review"
    )
    title = models.CharField(max_length=80, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    approved = models.BooleanField(default=False)

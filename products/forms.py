from django import forms
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]
        self.fields["category"].choices = display_names
        self.fields["old_price"].label = (
            "Old Price (Only needed if on sale is set)"
        )
        self.fields["on_sale"].label = "On Sale"
        self.fields["new_arrived"].label = "New Arrived"
        self.fields["image_url"].label = "Image URL"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ("approved",)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='shopping_bag'),
    path('add-item/<product_id>', views.add_item, name='add_item'),
]
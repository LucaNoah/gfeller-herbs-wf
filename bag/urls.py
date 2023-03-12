from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="shopping_bag"),
    path("add-item/<product_id>/", views.add_item, name="add_item"),
    path("edit-item/<product_id>/", views.edit_item, name="edit_item"),
]

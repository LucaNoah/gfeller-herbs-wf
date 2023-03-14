from django.urls import path
from . import views

urlpatterns = [
    path("", views.account, name="account"),
    path("add-feedback/", views.add_feedback, name="add_feedback"),
    path("feedbacks/", views.list_feedbacks, name="list_feedbacks"),
]

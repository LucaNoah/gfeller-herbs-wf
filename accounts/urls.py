from django.urls import path
from . import views

urlpatterns = [
    path("", views.account, name="account"),
    path("add-feedback/", views.add_feedback, name="add_feedback"),
    path("feedbacks/", views.list_feedbacks, name="list_feedbacks"),
    path("register-return/", views.add_return, name="add_return"),
    path("returns/", views.list_returns, name="list_returns"),
]

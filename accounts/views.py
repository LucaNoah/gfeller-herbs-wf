from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserAccount, CustomerFeedback
from .forms import UserAccountForm, FeedbackForm


@login_required
def account(request):
    """Display user account"""
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == "POST":
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account update was successful!")
    else:
        form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = "accounts/account.html"
    context = {
        "form": form,
        "orders": orders,
    }

    return render(request, template, context)


def list_feedbacks(request):
    """A view to display the customer feedbacks"""
    feedbacks = CustomerFeedback.objects.all()

    context = {
        "feedbacks": feedbacks,
    }

    return render(request, "accounts/feedbacks.html", context)


@login_required
def add_feedback(request):
    """View to render and save a customer feedback form"""
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback sent successfully!")
            return redirect(reverse("account"))
        else:
            messages.error(
                request,
                "Feedback could not be send, please check that the"
                " form is valid!",
            )
    else:
        form = FeedbackForm(initial={"user": request.user})

    template = "accounts/add_feedback.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
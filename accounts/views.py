from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required

from .models import UserAccount, CustomerFeedback, Return
from .forms import UserAccountForm, FeedbackForm, ReturnForm


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


@user_passes_test(lambda u: u.is_superuser)
def list_feedbacks(request):
    """A view to display the customer feedbacks"""
    feedbacks = CustomerFeedback.objects.all().order_by("-date")

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
                "Feedback could not be send, please check that the" " form is valid!",
            )
    else:
        form = FeedbackForm(initial={"user": request.user})

    template = "accounts/add_feedback.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def add_return(request):
    """View to register return by customer"""
    if request.method == "POST":
        form = ReturnForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Return registration sent successfully!")
            return redirect(reverse("account"))
        else:
            messages.error(
                request,
                "Return registration could not be send, please check that the"
                " form is valid!",
            )
    else:
        form = ReturnForm(initial={"user": request.user})
    account = get_object_or_404(UserAccount, user=request.user)
    orders = account.orders.all()

    template = "accounts/add_return.html"
    context = {
        "form": form,
        "orders": orders,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def list_returns(request):
    """A view to display the incoming returns"""
    returns = Return.objects.all().order_by("-date")

    context = {
        "returns": returns,
    }

    return render(request, "accounts/returns.html", context)

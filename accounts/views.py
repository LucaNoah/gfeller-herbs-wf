from django.shortcuts import render


def account(request):
    """
    Display user account
    """
    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)

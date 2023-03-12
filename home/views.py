from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return home page"""

    return render(request, "home/index.html")


def handle_404_page(request, exception):
    return render(request, "404_page.html")

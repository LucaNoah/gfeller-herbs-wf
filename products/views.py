from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to display all products as search queries and sorting"""

    products = Product.objects.all()

    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, 'You have not entered any search terms!')
                return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display the product's details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)
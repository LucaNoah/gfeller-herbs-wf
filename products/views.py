from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def list_products(request):
    """ A view to list either all products, specifically categorized products, or products requested by search query. """

    products = Product.objects.all()
    search_query = None
    categories_queried = None

    if request.GET:
        if 'category' in request.GET:
            categories_queried = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories_queried)
            categories_queried = Category.objects.filter(name__in=categories_queried)

        if 'query' in request.GET:
            search_query = request.GET['query']
            if not search_query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories_queried,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display the product's details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)
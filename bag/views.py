from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag content """
    
    return render(request, 'bag/shopping_bag.html')

def add_item(request, product_id):
    """ Add a certain number of an item to the shopping bag """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    bag = request.session.get('bag', {})

    if weight:
        if product_id in list(bag.keys()):
            if weight in bag[product_id]['items_by_weight'].keys():
                bag[product_id]['items_by_weight'][weight] += quantity
                messages.success(request, f'{weight} of {product.name} was successfully updated to {bag[product_id]["items_by_weight"][weight]} in your shopping bag!')
            else:
                bag[product_id]['items_by_weight'][weight] = quantity
                messages.success(request, f'{weight} of {product.name} was successfully added to your shopping bag!')
        else:
            bag[product_id] = {'items_by_weight': {weight: quantity}}
            messages.success(request, f'{weight} of {product.name} was successfully added to your shopping bag!')
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
            messages.success(request, f'{product.name} was successfully updated to {bag[product_id]["items_by_weight"][weight]} in your shopping bag!')
        else:
            bag[product_id] = quantity
            messages.success(request, f'{product.name} was successfully added to your shopping bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_item(request, product_id):
    """ A view to change the number of an item or to remove it """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    weight = None
    if 'product_weight' in request.POST:
        weight = request.POST['product_weight']
    bag = request.session.get('bag', {})

    if weight:
        if quantity > 0:
            bag[product_id]['items_by_weight'][weight] = quantity
            messages.success(request, f'{weight} of {product.name} was successfully updated to {bag[product_id]["items_by_weight"][weight]} in your shopping bag!')
        else:
            del bag[product_id]['items_by_weight'][weight]
            if not bag[product_id]['items_by_weight']:
                bag.pop(product_id)
                messages.success(request, f'{weight} of {product.name} was successfully removed from your shopping bag!')
    else:
        if quantity > 0:
            bag[product_id] = quantity
            messages.success(request, f'{product.name} was successfully updated to {bag[product_id]["items_by_weight"][weight]} in your shopping bag!')
        else:
            bag.pop(product_id)
            messages.success(request, f'{product.name} was successfully removed from your shopping bag!')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))
from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag content """
    
    return render(request, 'bag/shopping_bag.html')

def add_item(request, product_id):
    """ Add a certain number to the shopping bag """

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
            else:
                bag[product_id]['items_by_weight'][weight] = quantity
        else:
            bag[product_id] = {'items_by_weight': {weight: quantity}}
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += quantity
        else:
            bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

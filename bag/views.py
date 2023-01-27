from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the shopping bag content """
    
    return render(request, 'bag/shopping_bag.html')

def add_item(request, product_id):
    """ Add a certain number to the shopping bag """

    quanity = int(request.POST.get('quanity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quanity
    else:
        bag[product_id] = quanity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_content(request):

    bag_items = []
    total = 0
    bag_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += product.price * quantity
        bag_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery_cost = 0
        free_delivery_difference = 0

    grand_total = delivery_cost + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'bag_count': bag_count,
        'delivery_cost': delivery_cost,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .emails import send_conformation_email
from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from bag.contexts import bag_content
from accounts.forms import UserAccountForm
from accounts.models import UserAccount

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
   
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'email_address': request.POST['email_address'],
            'phone_number': request.POST['phone_number'],
            'full_name': request.POST['full_name'],
            'delivery_address': request.POST['delivery_address'],
            'town_or_city': request.POST['town_or_city'],
            'zip_code': request.POST['zip_code'],
            'state': request.POST['state'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for weight, quantity in item_data['items_by_weight'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_weight=weight,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'The form was not filled out correctly, \
                 please check the information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There is currently nothing in your shopping bag')
            return redirect(reverse('products'))

        current_bag = bag_content(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                account = UserAccount.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': account.default_full_name,
                    'delivery_address': account.default_delivery_address,
                    'town_or_city': account.default_town_or_city,
                    'town_or_city': account.default_town_or_city,
                    'zip_code': account.default_zip_code,
                    'state': account.default_state,
                    'country': account.default_country,
                })
            except UserAccount.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successfull checkouts """
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        # Attach user account to order
        account = UserAccount.objects.get(user=request.user)
        order.user_account = account
        order.save()

    send_conformation_email(order)
    messages.success(request, f'Order successfull! \
        Your order number is {order_number}. \
        Confirmation email sent to {order.email_address}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
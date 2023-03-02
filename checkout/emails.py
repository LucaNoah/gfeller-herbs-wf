from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_conformation_email(order):
    """Send confirmation email to customer"""

    recipient_email = order.email_address
    subject = render_to_string(
        'checkout/emails/order_confirmation_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/emails/order_confirmation_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email]
    )
from django.test import TestCase
from django.test import Client
from django.shortcuts import reverse
from .models import Order


class CheckoutViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/checkout/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reverse("products"), response.url)

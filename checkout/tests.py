from django.test import TestCase
from django.test import Client
from django.shortcuts import reverse
from .models import Order


class CheckoutViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get('/checkout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reverse('products'), response.url)


# class CheckoutSuccessTestCase(TestCase):
#     def setUp(self):
#         self.order = Order.objects.create(
#             email_address='test@test.com',
#             full_name='testy mctesten',
#             delivery_address='testaddress',
#             town_or_city='testcity',
#             country='testcountry',
#         )

#     def test_load_view(self):
#         c = Client()
#         print(self.order.order_number)
#         response = c.get(f'/checkout_success/{self.order.order_number}/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'products/products.html')
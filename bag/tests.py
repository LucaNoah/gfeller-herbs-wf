from django.test import TestCase
from django.test import Client
from products import models as products_model


class ViewBagTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/bag/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bag/shopping_bag.html")


# class AddItemTestCase(TestCase):
#     def setUp(self):
#         self.product = products_model.Product.objects.create(
#             name="testproduct",
#             description="some product",
#             price=123,
#             )

#     def test_load_view(self):
#         c = Client()
#         response = c.get(f"/bag/add-item/{self.product.id}/")
#         print(response.url)

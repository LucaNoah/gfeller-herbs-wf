from django.test import TestCase
from django.test import Client
from django.contrib.auth import models
from django.shortcuts import reverse
from products import models as products_model


class ListProductsTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")


class AddProductTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/products/add/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(f"/accounts/login/?next=/products/add/", response.url)


class EditProductTestCase(TestCase):
    def setUp(self):
        self.product = products_model.Product.objects.create(
            name="testproduct",
            description="some product",
            price=123,
        )

    def test_load_view(self):
        c = Client()
        response = c.get(f"/products/edit/{self.product.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            f"/accounts/login/?next=/products/edit/{self.product.id}/",
            response.url,
        )


class DeleteProductTestCase(TestCase):
    def setUp(self):
        self.product = products_model.Product.objects.create(
            name="testproduct",
            description="some product",
            price=123,
        )

    def test_load_view__anonymous_user(self):
        c = Client()
        response = c.get(f"/products/delete/{self.product.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            f"/accounts/login/?next=/products/delete/{self.product.id}/",
            response.url,
        )

    def test_load_view__superuser(self):
        user = models.User.objects.create_superuser("test", password="pass")
        c = Client()
        c.force_login(user)
        response = c.get(f"/products/delete/{self.product.id}/")
        self.assertEqual(response.status_code, 302)
        self.assertEquals(reverse("products"), response.url)

        product = products_model.Product.objects.filter(
            id=self.product.id
        ).first()
        self.assertEqual(product, None)


class AddReviewViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/products/add-review/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/products/add-review/", response.url
        )

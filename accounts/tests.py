from django.test import TestCase
from django.test import Client


class AccountViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/account/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual("/accounts/login/?next=/account/", response.url)

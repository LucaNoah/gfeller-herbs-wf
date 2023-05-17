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


class ListFeedbacksViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/account/feedbacks/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/account/feedbacks/", response.url
        )


class AddFeedbackViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/account/add-feedback/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/account/add-feedback/", response.url
        )


class AddReturnViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/account/register-return/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/account/register-return/", response.url
        )


class ListReturnsViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_load_view(self):
        c = Client()
        response = c.get("/account/returns/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            "/accounts/login/?next=/account/returns/", response.url
        )

from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.index_url = "/"
        self.sign_in_url = "/login"
        self.sign_out_url = "/logout"

    def test_index_authenticated(self):
        """
        Test index page is accessible when authenticated
        """

        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)

    def test_index_unauthenticated(self):
        """
        Test index page is not accessible when unauthenticated
        """

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 302)

    def test_sign_in_success(self):
        """
        Test successful sign in redirects to index page
        """

        response = self.client.post(
            self.sign_in_url, {"username": "testuser", "password": "12345"}
        )

        self.assertEqual(response.status_code, 302)

    def test_sign_out(self):
        """
        Test sign out redirects to login page
        """

        self.client.login(username="testuser", password="12345")
        response = self.client.get(self.sign_out_url)

        self.assertEqual(response.status_code, 302)

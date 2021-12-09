from django.test import TestCase, Client
from Application.models import User


class TestLogin(TestCase):
    def setUp(self):
        user = User(username="user1", email="user1@gmail.com")
        user.set_password("12345678")
        user.save()
        self.user = user
        self.client = Client()

    def test_login(self):
        response = self.client.post('/', {'j_username': self.user.email, 'j_password': self.user.password})
        self.assertEqual(response.url, '/accounts/login/?next=/',
                         'Incorrect redirect after the existing user logged in')
        response = self.client.get('accounts/login/?next=/')

    def test_invalidLogin(self):
        response = self.client.post('/', {'j_username': self.user.email, 'j_password': 4215165}, follow=True)
        self.assertTrue(response.status_code == 200)

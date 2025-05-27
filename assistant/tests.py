from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.username = 'testuser'
        cls.password = 'secretpassword123'
        cls.user = User.objects.create_user(username=cls.username, password=cls.password)

    def test_login_page_loads(self):
        response = self.client.get(reverse('assistant:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('assistant:login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('assistant:dashboard'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('assistant:login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password", status_code=200)


from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='andrii',
            email = 'pariri6288@yehudabx.com',
            password = 'testpass123',
        )
        self.assertEqual(user.username, 'andrii')
        self.assertEqual(user.email, 'pariri6288@yehudabx.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email = 'pariri6288@yehudabx.com',
            password = 'testpass123',
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'pariri6288@yehudabx.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(200, self.response.status_code)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there!')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )



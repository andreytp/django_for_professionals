from django.test import TestCase
from django.contrib.auth import get_user_model


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

    


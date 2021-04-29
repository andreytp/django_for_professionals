from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse

from .models import Book, Review


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )

        self.user = get_user_model().objects.create(
            username='testuser',
            email='testuser@email.com',
            password='testpass123',
        )
        self.special_permission = Permission.\
            objects.get(codename='special_status')

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual('Harry Potter', f'{self.book.title}')
        self.assertEqual('JK Rowling', f'{self.book.author}')
        self.assertEqual('25.00', f'{self.book.price}')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(302, response.status_code)
        self.assertRedirects(
            response,
            f'{reverse("account_login")}?next=/books/'
            )
        response = self.client.get(
            f'{reverse("account_login")}?next=/books/'
        )
        self.assertContains(response, 'Login page')

    def test_book_list_view_for_logged_in_user(self):
        self.client.logout()
        print(
            "Login success:",
            self.client.login(
                email='testuser@email.com',
                password='testpass123'))
        response = self.client.get(reverse('book_list'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view_with_permissions(self):
        self.client.logout()
        print(
            "Login success:",
            self.client.login(
                email='testuser@email.com',
                password='testpass123'))
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/123/detail')
        self.assertEqual(200, response.status_code)
        self.assertEqual(404, no_response.status_code)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')


# Create your tests here.

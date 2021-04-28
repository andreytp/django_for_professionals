from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title = 'Harry Potter',
            author = 'JK Rowling',
            price='25.00',
        )
    
    def test_book_listing(self):
        self.assertEqual('Harry Potter', f'{self.book.title}')
        self.assertEqual('JK Rowling', f'{self.book.author}')
        self.assertEqual('25.00', f'{self.book.price}')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/123/detail')
        self.assertEqual(200, response.status_code)
        self.assertEqual(404, no_response.status_code)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_detail.html')


# Create your tests here.

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from author.models import Author
from author.serializers import AuthorSerializer
from book.models import Book


class BookTests(APITestCase):

    url = reverse("books")

    def test_list_books(self):
        mommy.make(Book, make_m2m=True, _quantity=10)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_a_book(self):
        author = mommy.make(Author, name="Ramon Rodrigues")

        data = {
            "name": "My test to work in Olist \o/",
            "edition": 1,
            "publication_year": 2020,
            "authors": [author.id],
        }

        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_retrieve_a_book(self):
        mommy.make(Book, make_m2m=True, _quantity=10)
        url = reverse("book", kwargs={"pk": 5})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), 5)

    def test_update_book(self):
        mommy.make(Book, make_m2m=True, name="Crack the coding interview")
        url = reverse("book", kwargs={"pk": 1})

        book = Book.objects.get(pk=1)

        self.assertEqual(book.name, "Crack the coding interview")

        data = {
            "pk": book.pk,
            "name": "Obey the testing goat",
            "edition": book.edition,
            "publication_year": book.publication_year,
            "authors": list(book.authors.values_list("id", flat=True)),
        }

        response = self.client.put(url, data, format="json")

        book.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.name, "Obey the testing goat")

    def test_partial_update_book(self):
        mommy.make(Book, name="Crack the coding interview")
        url = reverse("book", kwargs={"pk": 1})

        book = Book.objects.get(pk=1)

        self.assertEqual(book.name, "Crack the coding interview")

        data = {"name": "Obey the testing goat"}

        response = self.client.patch(url, data, format="json")

        book.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(book.name, "Obey the testing goat")

    def test_delete_book(self):
        mommy.make(Book)
        url = reverse("book", kwargs={"pk": 1})

        self.assertEqual(Book.objects.count(), 1)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

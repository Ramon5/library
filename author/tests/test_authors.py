from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from author.models import Author


class AuthorTests(APITestCase):

    url = "/authors/"

    def test_get_authors(self):
        mommy.make(Author, _quantity=10)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.count(), 10)

    def test_create_author(self):

        data = {"name": "Fulano de Tal"}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)

    def test_fail_to_try_create_none_name_author(self):
        data = {"name": None}
        response = self.client.post(self.url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Author.objects.count(), 0)


    def test_retrieve_one_single_author(self):
        mommy.make(Author, _quantity=5)
        url = "/authors/{}/".format(3)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("id"), 3)


    def test_retrieve_inexistent_author(self):
        mommy.make(Author, _quantity=5)
        url = "/authors/{}/".format(6)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)        


    def test_update_a_author(self):
        mommy.make(Author, name="Roberto Souza")
        url = "/authors/{}/".format(1)

        author = Author.objects.get(pk=1)

        self.assertEqual(author.name, "Roberto Souza")

        data = {"name": "Ramon Rodrigues"}

        response = self.client.put(url, data, format="json")

        author.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.name, "Ramon Rodrigues")

    def test_delete_author(self):
        mommy.make(Author)
        url = "/authors/{}/".format(1)

        self.assertEqual(Author.objects.count(), 1)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), 0)

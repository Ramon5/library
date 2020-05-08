from rest_framework.serializers import ModelSerializer

from author.serializers import AuthorSerializer

from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "edition", "publication_year", "authors"]

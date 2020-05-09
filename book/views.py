from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookView(ModelViewSet):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("name", "edition", "publication_year", "authors")

    def get_queryset(self):
        return Book.objects.prefetch_related("authors").all()


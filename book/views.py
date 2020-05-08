from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .models import Book
from .serializers import BookSerializer


class BookCreateListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("name", "edition", "publication_year", "authors")

    def get_queryset(self):
        return Book.objects.prefetch_related("authors").all()


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

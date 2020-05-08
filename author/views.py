from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer


class AuthorCreateListView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        return Author.objects.all()


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        return Author.objects.all()

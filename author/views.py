from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer

class AuthorView(ModelViewSet):
    serializer_class = AuthorSerializer
    search_fields = ["name"]
    queryset = Author.objects.all()
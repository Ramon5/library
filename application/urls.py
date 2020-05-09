from django.urls import include, path
from django.contrib import admin

from rest_framework import routers
from author.views import AuthorView
from book.views import BookView

router = routers.DefaultRouter()
router.register(r"authors", AuthorView, basename="Author")
router.register(r"books", BookView, basename="Book")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]

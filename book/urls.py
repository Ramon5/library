from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^books/", views.BookCreateListView.as_view(), name="books"),
    url(
        r"^book/(?P<pk>\d+)/",
        views.BookRetrieveUpdateDestroyView.as_view(),
        name="book",
    ),
]

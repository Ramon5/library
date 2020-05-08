from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^authors/", views.AuthorCreateListView.as_view(), name="authors"),
    url(
        r"^author/(?P<pk>\d+)/",
        views.AuthorRetrieveUpdateDestroyView.as_view(),
        name="author",
    ),
]

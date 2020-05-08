from django.db import models

from author.models import Author


class Book(models.Model):
    name = models.CharField("Name", max_length=50)
    edition = models.IntegerField("Edition")
    publication_year = models.IntegerField("Publication Year")
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

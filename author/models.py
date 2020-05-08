from django.db import models


class Author(models.Model):
    name = models.CharField("Name", max_length=80, unique=True)

    def __str__(self):
        return self.name

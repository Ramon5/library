from django.db import models


class Author(models.Model):
    name = models.CharField("Name", max_length=80, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=["name",]),
        ]
    
    def __str__(self):
        return self.name

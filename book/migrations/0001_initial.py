# Generated by Django 3.0.6 on 2020-05-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("author", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("edition", models.IntegerField(verbose_name="Edition")),
                (
                    "publication_year",
                    models.IntegerField(verbose_name="Publication Year"),
                ),
                ("authors", models.ManyToManyField(to="author.Author")),
            ],
        )
    ]

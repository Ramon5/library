# Generated by Django 3.0.6 on 2020-05-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200508_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(verbose_name='Edition'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(verbose_name='Publication Year'),
        ),
    ]

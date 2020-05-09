# Generated by Django 3.0.6 on 2020-05-08 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(db_index=True, verbose_name='Edition'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(db_index=True, verbose_name='Publication Year'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]

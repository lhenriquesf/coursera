# Generated by Django 5.0.3 on 2024-03-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAPI', '0003_remove_book_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.SmallIntegerField(default=1),
        ),
    ]

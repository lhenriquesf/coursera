# Generated by Django 5.0.3 on 2024-03-14 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAPI', '0002_book_booksapi_bo_price_3901df_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='inventory',
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-20 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_drinks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='drink',
            new_name='drink_name',
        ),
    ]

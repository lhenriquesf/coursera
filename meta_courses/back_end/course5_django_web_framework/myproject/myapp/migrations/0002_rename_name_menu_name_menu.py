# Generated by Django 5.0.2 on 2024-02-20 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='name_menu',
        ),
    ]

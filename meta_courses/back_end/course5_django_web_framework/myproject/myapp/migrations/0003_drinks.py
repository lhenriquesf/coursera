# Generated by Django 5.0.2 on 2024-02-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_menu_name_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]

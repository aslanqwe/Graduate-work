# Generated by Django 4.2.1 on 2023-06-04 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_about_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forparents',
            name='image',
        ),
    ]
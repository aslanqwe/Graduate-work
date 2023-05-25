# Generated by Django 4.2.1 on 2023-05-23 13:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_articles_variable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='variable',
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(null=True, validators=[django.core.validators.MinLengthValidator(100, 'Введите больше 100 символов')], verbose_name='Статья'),
        ),
    ]
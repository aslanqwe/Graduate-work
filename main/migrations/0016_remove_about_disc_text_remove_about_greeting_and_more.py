# Generated by Django 4.2.1 on 2023-06-03 11:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_about_options_rename_image_about_image_one_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='disc_text',
        ),
        migrations.RemoveField(
            model_name='about',
            name='greeting',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image_two',
        ),
        migrations.RemoveField(
            model_name='clubs',
            name='disc_text',
        ),
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default='Введите название', max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='full_text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Изображение'),
        ),
    ]

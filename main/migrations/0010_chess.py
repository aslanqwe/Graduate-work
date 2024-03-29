# Generated by Django 4.2.1 on 2023-05-25 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_english_disc_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chess', models.CharField(max_length=15, verbose_name='Шахматы')),
                ('full_text', models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Описание кружка')),
                ('disc_text', models.TextField(default='', validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Доп.описание')),
                ('image', models.ImageField(default='', upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Шахматы',
                'verbose_name_plural': 'Шахматы',
            },
        ),
    ]

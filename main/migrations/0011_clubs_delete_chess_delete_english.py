# Generated by Django 4.2.1 on 2023-05-25 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_chess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_clubs', models.CharField(max_length=30, verbose_name='Название кружка')),
                ('full_text', models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Описание кружка')),
                ('disc_text', models.TextField(default='', validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Доп.описание')),
                ('image', models.ImageField(default='', upload_to='images/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Кружок',
                'verbose_name_plural': 'Кружки',
            },
        ),
        migrations.DeleteModel(
            name='Chess',
        ),
        migrations.DeleteModel(
            name='English',
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-25 07:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_director_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Ваше изображение'),
        ),
        migrations.AlterField(
            model_name='director',
            name='full_text',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, 'Введите больше 10 символов')], verbose_name='Приветственная речь'),
        ),
    ]

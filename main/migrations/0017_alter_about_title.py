# Generated by Django 4.2.1 on 2023-06-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_about_disc_text_remove_about_greeting_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]

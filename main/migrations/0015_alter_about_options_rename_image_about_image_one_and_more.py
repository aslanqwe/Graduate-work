# Generated by Django 4.2.1 on 2023-05-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_about_alter_forparents_disc_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='image_one',
        ),
        migrations.AddField(
            model_name='about',
            name='image_two',
            field=models.ImageField(default='', upload_to='images/', verbose_name='Доп.Изображение'),
        ),
    ]
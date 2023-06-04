from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from ckeditor.fields import RichTextField
class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = RichTextUploadingField('Статья', validators=[MinLengthValidator(10, 'Введите больше 10 символов')],
        blank=False, null=False)
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='images/', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class About(models.Model):
    title = models.CharField('Название', max_length=50, blank=True)
    full_text = RichTextField('Описание', validators=[MinLengthValidator(10, 'Введите больше 10 символов')],
        blank=False, null=False)
    image = models.ImageField('Изображение', upload_to='images/')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/about/{self.id}'
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Director(models.Model):
    full_name = models.CharField('ФИО', blank=False, null=False, max_length=70)
    full_text = RichTextField('Приветственная речь',
                                 validators=[MinLengthValidator(10, 'Введите больше 10 символов')], blank=False,
                                 null=False)
    image = models.ImageField('Ваше изображение', upload_to='images/', default='')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директор'



class Clubs(models.Model):
    name_clubs = models.CharField('Название кружка', blank=False, null=False, max_length=30)
    full_text = RichTextField('Описание кружка', validators=[MinLengthValidator(10, 'Введите больше 10 символов')],
                                 blank=False, null=False)
    image = models.ImageField('Изображение', upload_to='images/', default='')

    def __str__(self):
        return self.name_clubs

    def get_absolute_url(self):
        return f'/clubs/{self.id}'

    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'


class ForParents(models.Model):
    title = models.CharField('Название', blank=False, null=False, max_length=50)
    full_text = RichTextField('Описание', validators=[MinLengthValidator(10, 'Введите больше 10 символов')],
                                 blank=False, null=False)
    image = models.ImageField('Изображение', upload_to='images/', blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('for_parents', args=[self.title])

    class Meta:
        verbose_name = 'Для родителей'
        verbose_name_plural = 'Для родителей'

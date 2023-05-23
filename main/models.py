from django.db import models
from django.core.validators import MinLengthValidator


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья', validators = [MinLengthValidator(100, 'Введите больше 100 символов')], null = True)
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

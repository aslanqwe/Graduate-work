from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea, FileInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'date', 'image', ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'date': DateInput(format='%Y-%m-%dT%H:%M', attrs={
                'class': 'form-control',
                'type': 'datetime-local',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
            })
        }
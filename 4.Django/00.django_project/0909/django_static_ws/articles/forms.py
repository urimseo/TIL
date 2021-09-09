from django import forms
from django.db.models.fields.files import ImageField
from django.forms import widgets
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'max-length' : 10,
                'placeholder' : 'Enter the Title',
            }
        )
    )
    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter the Content',
            }

        )
    )
    class Meta:
        model = Article
        fields = '__all__'

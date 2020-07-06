from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'url']
        widgets = {
            "title" : forms.TextInput(attrs={"placeholder":"Write text, please"}),
            "text" : forms.Textarea(attrs={"placeholder":"Write text, please"}),
        }
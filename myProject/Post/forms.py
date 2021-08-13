from django import forms
from django.forms import fields
from.models import PostText


class PostTextForm(forms.ModelForm):
    class Meta:
        model=PostText
        fields=['text']
from django import forms
from .models import Tweet

class tweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        field = ['text','photo']
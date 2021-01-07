from django import forms
from django.conf import settings
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LEGHTH

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields = ['content']

    # for validation
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("Oops! this tweet is too long")
        return content
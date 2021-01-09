from rest_framework import serializers
from .models import Tweet
from django.conf import settings

MAX_TWEET_LENGTH = settings.MAX_TWEET_LEGHTH

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']
        
        def validate(self, value):
            if len(value)>MAX_TWEET_LENGTH:
                raise serializers.ValidationError("This tweet is too long")
            return value
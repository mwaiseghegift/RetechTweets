from rest_framework import serializers
from .models import Tweet
from django.conf import settings

MAX_TWEET_LENGTH = settings.MAX_TWEET_LEGHTH

TweetActionsOptions = settings.TWEET_ACTION_OPTIONS


class TweetCreateSerializer(serializers.ModelSerializer):
    
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes']
        
    def get_likes(self, obj):
        return obj.likes.count()
        
    def validate(self, value):
        if len(value)>MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value
    
class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'likes','is_retweet','parent']
        
    def get_likes(self, obj):
        return obj.likes.count()
    

        

        
class TweetActionSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)
    
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TweetActionsOptions:
            raise serializers.ValidationError('This is not a valid Action')
        return value
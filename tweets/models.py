from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

#for storing the time the likes were made and other functions 
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Use quotes if the related model is below
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, default=0, through=TweetLike)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_retweet(self):
       return self.parent != None
        
    def __str__(self):
        return self.content
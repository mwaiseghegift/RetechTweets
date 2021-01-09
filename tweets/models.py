import random
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']
    
    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes":random.randint(0,200)
        }
        
    def __str__(self):
        return self.content
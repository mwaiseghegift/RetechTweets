from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField(max_length=1000)
    image = models.FileField(upload_to='images/', blank=True, null=True)
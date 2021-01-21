from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL

# Create your views here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField() 
    location = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
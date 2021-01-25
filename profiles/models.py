from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save, post_save


User = settings.AUTH_USER_MODEL
# Create your models here.

class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField() 
    location = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    """
    Not that for auto_now = The time changes on update
                auto_now_add = The time does not change
    """
    
    def __str__(self):
        return self.user.username
    
def user_did_save(sender, instance, created, *args, **kwargs):
    Profile.objects.get_or_create(user=instance)
    if created:
        Profile.objects.get_or_create(user=instance)
    
post_save.connect(user_did_save, sender=User)
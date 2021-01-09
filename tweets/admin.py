from django.contrib import admin
from .models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email','content']
    list_display = ['user', 'content']
    
    class Meta:
        model = Tweet
    
admin.site.register(Tweet, TweetAdmin)
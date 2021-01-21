from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, Http404

from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def home_page_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    
    content = {
        "username":username
    }    
    
    return render(request, "home.html", content)

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id})







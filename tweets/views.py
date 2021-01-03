from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, Http404
from .forms import TweetForm

from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def HomepageView(request):
    tweets = Tweet.objects.all()

    data = {
        'tweets':tweets,
    }

    return render(request, 'home.html', data)

def TweetListView(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [{"id":i.id, "content":i.content, "image":i.image} for i in qs]
    
    data = {
        "response":tweet_list
    }

    return JsonResponse(data)

def TweetDetailView(request, tweet_id, *args, **kwargs):
    data = {
        "id":tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        data['image'] = obj.image
    except:
        data['message'] = "Not found"
        status = 404
    

    
    return JsonResponse(data, status=status)

def TweetCreateView(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()

    data = {
        'form':form,
    }

    return render(request, 'components/tweetform.html', data)

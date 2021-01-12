from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, Http404
from .forms import TweetForm

from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet

#rest framework
from rest_framework.response import Response
from .serializers import (TweetCreateSerializer, 
                          TweetSerializer, 
                          TweetActionSerializer)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def HomepageView(request):
    tweets = Tweet.objects.all()

    data = {
        'tweets':tweets,
    }

    return render(request, 'home.html', data)

@api_view(['POST'])  #http method is POST
@permission_classes([IsAuthenticated])
def TweetCreateView(request, *args, **kwargs):
    #Django Rest Framework CreateView
    serializer = TweetCreateSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status = 201)
    return Response({}, status = 400)
    
    
    #Normal CreateView
    """
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401) #not authorized
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    data = {
        'form':form,
    }

    return render(request, 'components/tweetform.html', data)
    """



#DRF list view

@api_view(['GET'])
def TweetListView(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data)


#Pure django list_view   
""" 
def TweetListView(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [i.serialize() for i in qs]
    
    data = {
        "response":tweet_list
    }

    return JsonResponse(data)
"""

@api_view(['GET'])
def TweetDetailView(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status = 200)

"""
def TweetDetailView(request, tweet_id, *args, **kwargs):
    data = {
        "id":tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    

    
    return JsonResponse(data, status=status)
"""

@api_view(['DELETE','POST'])
@permission_classes([IsAuthenticated])
def TweetDeleteView(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'message':'Sorry! You are not allowed to delete this'}, status=401) #forbidden
    obj = qs.first()
    obj.delete()
    return Response({'message':'Tweet Deleted'}, status=200) #ok

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TweetActionView(request, *args, **kwargs):
    """
    View for Tweet Actions which are: Like, Unlike, Retweet
    """
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
    
        qs = Tweet.objects.filter(id=tweet_id) 
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        
        if action == 'like':
             obj.likes.add(request.user)
             serializer = TweetSerializer(obj)
             return Response(serializer.data, status=200)
        elif action == 'unlike':
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == 'retweet':
            retweeted_tweet = Tweet.objects.create(user=request.user, 
                                                   parent=obj,
                                                   content=obj.content)
            serializer = TweetSerializer(retweeted_tweet)
            return Response(serializer.data, status=201)
           
    return Response({}, status=200)
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, Http404
from .forms import TweetForm

from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet

#rest framework
from rest_framework.response import Response
from .serializers import TweetSerializer
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
    serializer = TweetSerializer(data=request.POST)
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

@api_view(['POST'])  #http method is POSt
def TweetCreateView(request, *args, **kwargs):
    
    #Django Rest Framework CreateView
    data = request.POST
    serializer = TweetSerializer(data=data)
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

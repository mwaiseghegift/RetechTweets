from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, Http404


from django.utils.http import is_safe_url
from django.conf import settings
from ..models import Profile
from django.contrib.auth import get_user_model
#rest framework
from rest_framework.response import Response


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
@api_view(['GET','POST'])  #http method is POST
@permission_classes([IsAuthenticated])
def UserFollowView(request, username, *args, **kwargs):
    current_user = request.user
    user_to_follow = User.objects.filter(username=username)
    if user_to_follow.exists() == False:
        return Response({}, status=404)
    
    other = user_to_follow.first()
    profile= other.profile
    
    data = {}
    
    try:
        data = request.data
    except:
        pass
    print(data)
    action = data.get("action")
    
    if action == 'follow':
        profile.followers.add(current_user)
    elif action == 'unfollow':
        Profile.followers.remove(current_user)
    else:
        pass
    current_followers = profile.followers.all()
    
    return Response({"followers":current_followers.count()}, status = 200)
    
    
    
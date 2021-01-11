from django.urls import path
from .views import (
    HomepageView, 
    TweetCreateView, 
    TweetDetailView, 
    TweetListView,
    TweetDeleteView,
    TweetActionView,
)

urlpatterns = [
    path('', HomepageView, name='homepage'),
    path('create-tweet/', TweetCreateView, name='create-tweet'),
    path('tweets/', TweetListView, name='tweet-list'),
    path('tweet/action/', TweetActionView, name='tweet-action'),
    path('tweet/<int:tweet_id>/', TweetDetailView, name='tweet-detail'),
    path('tweet/<int:tweet_id>/delete/', TweetDeleteView, name='tweet-delete'),
    
    
]

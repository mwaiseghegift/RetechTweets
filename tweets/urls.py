from django.urls import path, re_path
from .views import (
    HomepageView, 
    TweetCreateView, 
    TweetDetailView, 
    TweetListView,
    TweetDeleteView,
)

urlpatterns = [
    path('', HomepageView, name='homepage'),
    path('create-tweet/', TweetCreateView, name='create-tweet'),
    path('tweets/', TweetListView, name='tweet-list'),
    path('tweet/<int:tweet_id>/', TweetDetailView, name='tweet-detail'),
    path('api/tweet/<int:tweet_id>/delete/', TweetDeleteView, name='tweet-delete')
    
]

from django.urls import path
from .views import (
    HomepageView, 
    TweetCreateView, 
    TweetDetailView, 
    TweetListView,
    TweetDeleteView,
    TweetActionView,
    TweetProfileView,
)

urlpatterns = [
    path('', HomepageView, name='homepage'),
    path('tweets/', TweetListView, name='tweet-list'),
    path('tweet/action/', TweetActionView, name='tweet-action'),
    path('tweet/create-tweet/', TweetCreateView, name='create-tweet'),
    path('tweet/<int:tweet_id>/', TweetDetailView, name='tweet-detail'),
    path('tweets/<int:tweet_id>/delete/', TweetDeleteView, name='tweet-delete'),

]

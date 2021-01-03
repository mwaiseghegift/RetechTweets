from django.urls import path, re_path
from .views import (
    HomepageView, TweetCreateView, TweetDetailView, TweetListView,
)

urlpatterns = [
    path('', HomepageView, name='homepage'),
    path('create-tweet/', TweetCreateView, name='create-tweet'),
    path('tweets/', TweetListView, name='tweet-list'),
    path('tweet/<int:tweet_id>/', TweetDetailView, name='tweet-detail'),
]

from django.urls import path
from .views import (
    home_page_view,
    tweets_detail_view,
    tweets_list_view,
    TweetProfileView,
    
)

urlpatterns = [
    path('', home_page_view, name='local-home'),
    path('list/', tweets_list_view, name='local_tweet_list' ),
    path('/<int:tweet_id>', tweets_detail_view, name='local_tweet_detail'),
    path('profile/<str:username>/', TweetProfileView, name='profile'),
    

    
]

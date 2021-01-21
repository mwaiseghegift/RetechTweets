from django.urls import path
from .views import (
    home_page_view,
    tweets_detail_view,
    tweets_list_view,

    
)

urlpatterns = [
    path('home', home_page_view, name='local-home'),
    path('', tweets_list_view, name='local_tweet_list' ),
    path('<int:tweet_id>/', tweets_detail_view, name='local_tweet_detail'),
    

    
]

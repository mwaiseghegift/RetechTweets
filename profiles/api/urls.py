from django.urls import path
from .views import (
    UserFollowView
)

urlpatterns = [
    path('<str:username>/follow/', UserFollowView, name='user-follow'),

]

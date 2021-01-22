from django.urls import path
from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    
)
app_name = 'profiles'

urlpatterns = [
    path('<str:username>', ProfileDetailView, name='profile'),
    path('update/', ProfileUpdateView, name='profile_update'),
]
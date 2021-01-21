from django.urls import path
from .views import (
    login_view,
    logout_view,
    UserCreationView,
)
app_name='accounts'

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view),
    path("register/", UserCreationView)  
]

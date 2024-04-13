from django.urls import path
from .views import UserRegister, AuthUser


urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', AuthUser.as_view())
]

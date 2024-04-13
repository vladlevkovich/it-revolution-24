from django.urls import path
from .views import *


urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', AuthUser.as_view()),
    path('access-token/', UpdateAccessToken.as_view())
]

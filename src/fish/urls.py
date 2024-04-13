from django.urls import path
from .views import *


urlpatterns = [
    path('feed-aquarium/', FeedAquarium.as_view()),
    path('aquarium/', AquariumReadCreate.as_view())
]


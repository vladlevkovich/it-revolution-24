from django.urls import path
from .views import *


urlpatterns = [
    path('feed-aquarium/', FeedAquarium.as_view(), name='feed-aquarium'),
    path('clean-aquarium/', CleanAquarium.as_view(), name='add-clean-record'),
    path('aquarium/', AquariumReadCreate.as_view()),
    path('fish/', AddFish.as_view()),
    path('algae/', AddAlgae.as_view()),
    path('shrimp/', AddShrimp.as_view())
]


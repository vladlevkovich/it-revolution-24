from django.urls import path
from .views import *


urlpatterns = [
    path('feed-aquarium/', FeedAquarium.as_view(), name='feed-aquarium'),
    path('clean-aquarium/', CleanAquarium.as_view(), name='add-clean-record'),
    path('aquarium/', AquariumReadCreate.as_view()),
    path('analytics/', Analytics.as_view()),
    path('fish/', AddFish.as_view()),
    path('fish-update/<uuid:pk>/', FishUpdate.as_view()),
    path('algae/', AddSnail.as_view()),
    path('algae-update/', AlgaeUpdate.as_view()),
    path('shrimp/', AddShrimp.as_view()),
    path('shrimp-update/<uuid:pk>/', ShrimpUpdate.as_view()),
    path('down/', downland_swagger)
]


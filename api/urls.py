# api/urls.py
from django.urls import path
from .views import FitnessPredictionAPI

urlpatterns = [
    path('fitness-prediction/', FitnessPredictionAPI.as_view(),
         name='fitness-prediction'),
]

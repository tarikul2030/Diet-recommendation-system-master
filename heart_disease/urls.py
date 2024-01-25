from django.urls import path
from . import views


urlpatterns = [
    path('hrt/', views.heart),

]

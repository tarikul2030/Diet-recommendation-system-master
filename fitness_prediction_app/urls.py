
from django.urls import path
from . import views


urlpatterns = [
    path('rms/', views.active),

]

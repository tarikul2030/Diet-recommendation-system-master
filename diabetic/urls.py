from django.urls import path
from . import views


urlpatterns = [
    path('diab/', views.diabetic),

]

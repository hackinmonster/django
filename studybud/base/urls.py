from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #passing in the id into the url, comes from the parameter in the room function in views.py
    #this allows for dynamic routing
    path('room/<str:pk>/', views.room, name='room'),
    
]
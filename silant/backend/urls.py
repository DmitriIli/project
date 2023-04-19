from django.urls import path, include
from . import views

urlpatterns = [
    path('api/index/', views.index),
    path('', views.getlist),
    
]

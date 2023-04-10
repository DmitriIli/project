from django.urls import path, include
from . import views

urlpatterns = [
    path('api/get/', views.get),
]

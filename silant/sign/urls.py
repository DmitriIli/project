from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views


urlpatterns = [
    path('sign/login/',
         LoginView.as_view(template_name='frontend/login.html'),
         name='login'),
    path('sign/logout/',
         LogoutView.as_view(template_name='frontend/logout.html'),
         name='logout'),
]

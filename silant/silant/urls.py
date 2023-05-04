from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    # path('', include('frontend.urls')),
    path('', include('sign.urls')),
    path('api/user/', views.user, name='user'),
    path('api/login/', views.auth_login, name='login'),
    path('api/logout/', views.auth_logout, name='logout'),
]

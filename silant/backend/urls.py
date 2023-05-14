from django.urls import path, include
from . import views

urlpatterns = [
    # path('api/index/', views.index),
    path('', views.getlist),
    path('service/<str:item>/', views.machine, name='machine'),
    path('catalog/<str:param>/', views.catalog, name='catalog'),
    path('api/get/', views.get_machines_by_users_group, name='get_machines_by_users_group'),
    
]

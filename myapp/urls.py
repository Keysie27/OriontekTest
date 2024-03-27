from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/list/', views.list_clients, name='list_clients'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/add_address/', views.add_address, name='add_address'),
]

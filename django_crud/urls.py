from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('create/', views.create_item, name='create_item'),
    path('read/', views.read_items, name='read_items'),
    path('update/', views.update_item, name='update_item'),
    path('delete/', views.delete_item, name='delete_item'),
]

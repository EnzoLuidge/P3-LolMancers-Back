from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user/', views.User, name='User'),
    path('api/user_operations/', views.User_operations, name='User_operations'),
    path('api/saved_player_operations/', views.Saved_player_operations, name='Saved_player_operations'),
]
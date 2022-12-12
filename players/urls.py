from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user/', views.User_player, name='User_player'),
    path('api/user_operations/', views.User_operations, name='User_operations'),
    path('api/saved_player_operations/', views.Saved_player_operations, name='Saved_player_operations'),
    path('api/login/', views.Login, name='Login'),
    path('api/logout/', views.Logout, name='Logout'),
    path('api/get_user/', views.Get_user, name='Get_user'),
    path('api/register/', views.Register, name='Register'),
]

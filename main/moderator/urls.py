from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="index"),
    path('games/', views.show_shop, name="show_shop"),
    path('create', views.show_create, name="create"),
    path('users/', views.show_users, name="show_users"),
    path('save_to_file/', views.save_users_to_file, name='save_users_to_file'),
    path('load_to_file/', views.load_users_from_file, name='load_users_from_file'),
    path('users/<int:pk>/delete', views.UserDeleteView.as_view(), name="user_delete"),
    path('games/<int:pk>/delete', views.GameDeleteView.as_view(), name="game_delete")

]




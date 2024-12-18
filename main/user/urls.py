from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_index, name="index"),
    path('games', views.show_games, name="games"),
    path('account', views.show_account, name="account")
]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_index),
    path('games', views.show_games),
    path('account', views.show_account)
]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_index, name="index"),
    path('shop', views.show_shop, name="shop"),
    path('games', views.show_games, name="games"),
    path('community', views.show_community, name="community"),
    path('account', views.show_account, name="account"),
]


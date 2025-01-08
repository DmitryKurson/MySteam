from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.show_index, name="index"),
    path('shop', views.show_shop, name="shop"),
    path('games', views.show_games, name="games"),
    path('community', views.show_community, name="community"),
    path('<int:user_id>/account', views.show_account, name="account"),
    path('login/', views.show_login, name="login"),
    path('create', views.show_create, name="create")
]


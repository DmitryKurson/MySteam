from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name="index"),
    path('shop/', views.show_shop, name="show_shop"),
    path('community/', views.show_community, name="show_community"),
    path('users/', views.show_users, name="show_users"),
    path('users/<int:pk>/delete', views.UserDeleteView.as_view(), name="user_delete")

]




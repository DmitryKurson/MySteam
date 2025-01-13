from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_index, name="index_m"),
    path('shop/', views.show_shop, name="show_shop"),
    path('community/', views.show_community, name="show_community")

]




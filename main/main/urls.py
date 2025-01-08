from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcomepage, name="index"),
    path('user/', include('user.urls')),
    path('moderator/', include('moderator.urls'))
]

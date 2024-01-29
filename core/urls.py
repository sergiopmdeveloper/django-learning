from django.contrib.auth import views as auth_views
from django.urls import path

from core.views import index

urlpatterns = [
    path("", index, name="index"),
    path("login", auth_views.LoginView.as_view(), name="login"),
]

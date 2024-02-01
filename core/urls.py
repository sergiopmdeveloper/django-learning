from django.urls import path

from core.views import index, sign_in, sign_out, sign_up

urlpatterns = [
    path("", index, name="index"),
    path("login", sign_in, name="login"),
    path("register", sign_up, name="register"),
    path("logout", sign_out, name="logout"),
]

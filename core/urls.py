from django.urls import path

from core.views import index, sign_in, sign_out

urlpatterns = [
    path("", index, name="index"),
    path("login", sign_in, name="login"),
    path("logout", sign_out, name="logout"),
]

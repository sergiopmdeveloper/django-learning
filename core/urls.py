from django.urls import path

from core.views import index, sign_in

urlpatterns = [
    path("", index, name="index"),
    path("login", sign_in, name="login"),
]

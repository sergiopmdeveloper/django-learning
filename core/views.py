from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def index(request: HttpRequest) -> HttpResponse:
    """
    View for the index page.
    """

    return render(request, "core/index.html")


def login(request: HttpRequest) -> HttpResponse:
    """
    View for the sign in page.
    """

    form_errors = {}

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            # TODO: Authenticate user
            ...
        else:
            form_errors["username"] = form.errors.get("username", [None])[0]
            form_errors["password"] = form.errors.get("password", [None])[0]

            return render(
                request,
                "registration/login.html",
                {
                    "form_errors": form_errors,
                    "username": request.POST["username"],
                    "password": request.POST["password"],
                },
            )

    return render(request, "registration/login.html", {"form_errors": form_errors})

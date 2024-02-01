from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm


@login_required()
def index(request: HttpRequest) -> HttpResponse:
    """
    View for the index page.
    """

    return render(request, "core/index.html")


def sign_in(request: HttpRequest) -> HttpResponse:
    """
    View for the sign in page.
    """

    if request.user.is_authenticated:
        return redirect("/")

    form_errors = {}

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return redirect("/")

            else:
                return render(
                    request,
                    "registration/login.html",
                    {
                        "invalid_credentials": True,
                    },
                )

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

    return render(request, "registration/login.html")


def sign_up(request: HttpRequest) -> HttpResponse:
    """
    View for the sign up page.
    """

    if request.user.is_authenticated:
        return redirect("/")

    return render(request, "registration/register.html")


def sign_out(request: HttpRequest) -> HttpResponse:
    """
    View for logging out.
    """

    logout(request)

    return redirect("login")

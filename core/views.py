from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm


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

    form_errors = {}

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                new_user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )

            except IntegrityError:
                return render(
                    request,
                    "registration/register.html",
                    {
                        "user_already_exists": True,
                    },
                )

            new_user.save()

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return redirect("/")

            else:
                return render(
                    request,
                    "registration/register.html",
                    {
                        "register_error": True,
                    },
                )

        else:
            form_errors["username"] = form.errors.get("username", [None])[0]
            form_errors["first_name"] = form.errors.get("first_name", [None])[0]
            form_errors["last_name"] = form.errors.get("last_name", [None])[0]
            form_errors["email"] = form.errors.get("email", [None])[0]
            form_errors["password"] = form.errors.get("password", [None])[0]

            return render(
                request,
                "registration/register.html",
                {
                    "form_errors": form_errors,
                    "username": request.POST["username"],
                    "first_name": request.POST["first_name"],
                    "last_name": request.POST["last_name"],
                    "email": request.POST["email"],
                    "password": request.POST["password"],
                },
            )

    return render(request, "registration/register.html")


def sign_out(request: HttpRequest) -> HttpResponse:
    """
    View for logging out.
    """

    logout(request)

    return redirect("login")

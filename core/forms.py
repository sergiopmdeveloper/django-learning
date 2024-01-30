from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    """
    Login form validator
    """

    class Meta:
        model = User
        fields = ["username", "password"]
        error_messages = {
            "username": {
                "required": "Required",
            },
            "password": {
                "required": "Required",
            },
        }

from django import forms


class LoginForm(forms.Form):
    """
    Login form validator
    """

    username = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )
    password = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )

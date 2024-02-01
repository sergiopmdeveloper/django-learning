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


class RegisterForm(forms.Form):
    """
    Register form validator
    """

    username = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )
    first_name = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )
    last_name = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Required",
            "invalid": "Invalid email",
        },
    )
    password = forms.CharField(
        required=True,
        error_messages={
            "required": "Required",
        },
    )

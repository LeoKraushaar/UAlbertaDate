from django import forms
from django.contrib.auth.models import User
from validators import email_validator

class SignUpForm(forms.ModelForm):

    email = forms.EmailField(
        validators=[email_validator]
    )

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        exclude = [
            "username"
        ]

    
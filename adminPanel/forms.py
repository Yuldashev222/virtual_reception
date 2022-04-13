from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


# captcha = CaptchaField()


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
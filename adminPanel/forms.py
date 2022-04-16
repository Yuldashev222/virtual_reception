from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class AddUserForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text='Yangi takrorlanmagan ism yarating', label="Username")
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]


class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'photo',
            'info',
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'info': forms.TextInput(attrs={'class':'form-control'}),
        }

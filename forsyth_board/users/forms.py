from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        try:
            fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
        except:
            exclude = ('user_permissions', 'date_joined', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'groups', 'password')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        try:
            fields = ('username', 'email', 'first_name', 'last_name',)
        except:
            exclude = ('user_permissions', 'date_joined', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'groups', 'password', 'password1', 'password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user_permissions', 'date_joined', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'groups', 'password', 'password1', 'password2', 'id_username', 'username', 'id_email', 'email', 'first_name', 'last_name', 'user')
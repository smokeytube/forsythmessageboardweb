from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import fields_for_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        try:
            fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
        except:
            exclude = ('user_permissions', 'date_joined', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'groups', 'password')

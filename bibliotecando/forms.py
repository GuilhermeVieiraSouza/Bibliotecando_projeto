from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models

class UserForm(UserCreationForm):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'imagem', 'data_nascimento',  'password1', 'password2']

        
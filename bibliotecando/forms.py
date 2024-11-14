from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models

class UserForm(UserCreationForm):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'imagem', 'data_nascimento',  'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'placeholder': 'Imagem'}), 
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha', 'type': 'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmação de Senha'}),
        }
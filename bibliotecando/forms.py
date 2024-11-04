from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagem'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data de Nascimento'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'imagem', 'data_nascimento', 'endereco', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmação de Senha'}),
        }
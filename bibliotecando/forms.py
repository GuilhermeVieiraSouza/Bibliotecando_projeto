from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from . import models

class UserForm(UserCreationForm):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'imagem', 'data_nascimento',  'password1', 'password2']

class UserEditForm(UserChangeForm):
    class Meta:
        model = models.Usuario
        fields = ['username', 'email', 'imagem', 'data_nascimento']


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = ['texto', 'nota']  # Inclua os campos que o usuário preencherá

        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Escreva seu comentário...', 'rows': 3}),
            'nota': forms.NumberInput(attrs={'min': 1, 'max': 5, 'step': 1}),  # Para nota entre 1 e 5
        }
from django import forms
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
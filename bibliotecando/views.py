from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models
from . import forms
# Create your views here.
def descubra(request):
    livros = models.Livro.objects.all()
    return render(request, 'bibliotecando/descubra.html', {'livros': livros})

def MeusLivros(request):
    models.Favoritos.objects.all()
    return render(request, 'bibliotecando/meusLivros.html')

def detalhesLivro(request, id):
    livro = models.Livro.objects.get(id=id)
    comentarios = models.Comentario.objects.filter(livro=livro)
    contexto = {
        'livro': livro,
        'publicacao': f"{livro.data_publicacao.day}/{livro.data_publicacao.month}/{livro.data_publicacao.year}",
        'comentarios': comentarios
        }
    return render(request, 'bibliotecando/detalhesLivro.html', contexto)


#Sistema de login
def register(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('bibliotecando:login')
    else:
        form = forms.UserForm()

    return render(request, 'bibliotecando/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gerencia:gerencia_inicial')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

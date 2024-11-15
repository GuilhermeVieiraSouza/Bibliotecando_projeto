from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
def descubra(request):
    livros = models.Livro.objects.all()
    return render(request, 'bibliotecando/descubra.html', {'livros': livros})

@login_required(login_url='bibliotecando:login')
def MeusLivros(request):
    models.Favoritos.objects.all()
    return render(request, 'bibliotecando/meusLivros.html')

def detalhesLivro(request, id):
    livro = models.Livro.objects.get(id=id)
    comentarios = models.Comentario.objects.filter(livro=livro)
    links = models.Links.objects.filter(livro=livro)
    contexto = {
        'livro': livro,
        'publicacao': f"{livro.data_publicacao.day}/{livro.data_publicacao.month}/{livro.data_publicacao.year}",
        'comentarios': comentarios,
        'links': links
        }
    return render(request, 'bibliotecando/detalhesLivro.html', contexto)

@login_required(login_url='bibliotecando:login')
def profile(request):
    usuario = request.user
    imagem = models.Usuario.objects.get(username=usuario.username).imagem
    context = {
        'usuario': usuario,
        'imagem': imagem
    }
    return render(request, 'bibliotecando/profile.html', context)

@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = forms.UserEditForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('bibliotecando:profile') 
        else:
            
            print(form.errors) 
    else:
        form = forms.UserEditForm(instance=usuario)
    return render(request, 'bibliotecando/editarUsuario.html', {'form': form})

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
        print(username)

        if user is not None:
            login(request,user)
            
            return redirect('bibliotecando:descubra')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'bibliotecando/login.html')

def logout_view(request):
    logout(request)
    return redirect('bibliotecando:login')

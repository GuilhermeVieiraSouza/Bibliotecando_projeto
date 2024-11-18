from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from django.core.paginator import Paginator


# Create your views here.
def descubra(request):
    livros = models.Livro.objects.all()
    return render(request, 'bibliotecando/descubra.html', {'livros': livros})


def detalhesLivro(request, id):
    livro = models.Livro.objects.get(id=id)
    comentarios = models.Comentario.objects.filter(livro=livro).order_by('data')
    links = models.Links.objects.filter(livro=livro)
    categorias = models.Categoria.objects.filter(livro_categoria=livro)
    paginator = Paginator(comentarios, 3)  # 10 usuários por página
    
    page = request.GET.get('page', 1)
    try:
        comentarios = paginator.page(page)
    except:
        comentarios = paginator.page(1)


    favorito = None
    if request.user.is_authenticated:
        favorito = models.Favoritos.objects.filter(usuario=request.user, livro=livro).exists()
    if request.method == "POST" and request.user.is_authenticated:
        action = request.POST.get('action')
        if action == "toggle_favorito":
            if favorito:
                models.Favoritos.objects.filter(usuario=request.user, livro=livro).delete()
                favorito = False
            else:
                models.Favoritos.objects.create(usuario=request.user, livro=livro)
                favorito = True
            return JsonResponse({'favorito': favorito})

    if request.method == "POST" and request.user.is_authenticated:
        form = forms.ComentarioForm(request.POST)
        if form.is_valid():  
            comentario = form.save(commit=False)
            comentario.livro = livro
            comentario.usuario = request.user  # Associa o usuário logado
            comentario.save()
            return redirect('bibliotecando:detalhesLivro', id=id)
    else:
        form = forms.ComentarioForm()

    

    contexto = {
        'stars_range': range(1, 6),
        'autenticado': request.user.is_authenticated,
        'livro': livro,
        'publicacao': f"{livro.data_publicacao.day}/{livro.data_publicacao.month}/{livro.data_publicacao.year}",
        'comentarios': comentarios,
        'links': links,
        'categorias': categorias,
        'favorito': favorito,
        }
    return render(request, 'bibliotecando/detalhesLivro.html', contexto)

@login_required(login_url='bibliotecando:login')
def MeusLivros(request):
    favoritos = models.Favoritos.objects.filter(usuario=request.user)
    context = {
        'favoritos': favoritos
    }
    return render(request, 'bibliotecando/meusLivros.html', context)

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
        form = forms.UserForm(request.POST, request.FILES)
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
            login(request,user)
            
            return redirect('bibliotecando:descubra')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'bibliotecando/login.html')

def logout_view(request):
    logout(request)
    return redirect('bibliotecando:login')

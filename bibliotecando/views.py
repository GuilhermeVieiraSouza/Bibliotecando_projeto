from django.shortcuts import render, redirect
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

def login(request):
    if request.method == 'POST':
        form = forms.UsuarioForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('cadastro_sucesso')  
    else:
        form = forms.UsuarioForm()

    contexto = {
        'form': form
        }
    return render(request, 'bibliotecando/registro.html', contexto)
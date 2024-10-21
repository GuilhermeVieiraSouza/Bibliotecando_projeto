from django.shortcuts import render
from . import models
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
from django.shortcuts import render
from . import models
# Create your views here.
def descubra(request):
    livros = models.Livro.objects.all()
    return render(request, 'descubra.html', {'livros': livros})

def MeusLivros(request):
    models.Favoritos.objects.all()
    return render(request, 'meusLivros.html')
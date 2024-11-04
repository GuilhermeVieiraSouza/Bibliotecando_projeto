from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['userName', 'email', 'data_nascimento']
    search_fields = ['userName', 'email', 'data_nascimento']
    list_filter = ['data_nascimento']

@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(models.Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_publicacao']
    search_fields = ['titulo', 'autor', 'data_publicacao']
    list_filter = ['data_publicacao']

@admin.register(models.Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ['url', 'livro']
    search_fields = ['url', 'livro']
    list_filter = ['livro']

@admin.register(models.Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['livro', 'usuario', 'texto']
    search_fields = ['livro', 'usuario', 'texto']
    list_filter = ['usuario']

@admin.register(models.Favoritos)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = ['livro', 'usuario']
    search_fields = ['livro', 'usuario']
    list_filter = ['usuario']

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(models.Preferencias)
class PreferenciasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'categoria']
    search_fields = ['usuario', 'categoria']
    list_filter = ['usuario']




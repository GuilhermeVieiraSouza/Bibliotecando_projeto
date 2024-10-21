from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    imagem = models.ImageField(upload_to='usuarios/', blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nome} {self.email} {self.senha}'

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    biografia = models.TextField()
    data_nascimento = models.DateField()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f'{self.nome} {self.data_nascimento}'
    
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='imagens/')
    descricao = models.TextField()
    data_publicacao = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return f'{self.titulo} {self.data_publicacao}'
    
class Links(models.Model):
    url = models.URLField()
    nome = models.CharField(max_length=255, blank=True, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
    def __str__(self):
        return f'{self.url} {self.Livro}'
    
class Comentario(models.Model):
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    nota = models.IntegerField()
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f'{self.texto} {self.data} {self.livro}'
    
class Favoritos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'

    def __str__(self):
        return f'{self.usuario} {self.livro}'
    
class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    livro_categoria = models.ManyToManyField(Livro)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.nome} {self.descricao}'
    
class Preferencias(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Preferencia'
        verbose_name_plural = 'Preferencias'

    def __str__(self):
        return f'{self.usuario} {self.categoria}'
    


    
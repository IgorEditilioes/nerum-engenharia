from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    git_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
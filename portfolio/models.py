from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao_curta = models.CharField(max_length=300)
    descricao_detalhada = models.TextField()
    imagem_principal = models.ImageField(upload_to='projetos/capa/')
    video_url = models.URLField(blank=True, null=True)
    git_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    
class ProjetoImagens(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='projetos/galeria/')

    def __str__(self):
        return f"Imagem de {self.projeto.titulo}"


class Orcamento(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orçamento de {self.nome} - {self.email}"
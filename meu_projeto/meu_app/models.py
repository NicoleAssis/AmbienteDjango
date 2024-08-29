from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

class Feedback(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    colaborador = models.CharField(max_length=100)
    avaliacao = models.IntegerField()
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

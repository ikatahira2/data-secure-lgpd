# coleta_dados/models.py

from django.db import models

class DadosUsuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    consentimento = models.BooleanField(default=False)
    data_submissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

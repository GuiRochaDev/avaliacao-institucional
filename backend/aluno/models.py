from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
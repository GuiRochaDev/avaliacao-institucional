from django.db import models

class disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(unique=True)
    professor = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
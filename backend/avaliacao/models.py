from django.db import models
from aluno.models import aluno
from disciplina.models import disciplina


class avaliacao(models.Model):
    nota = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ("PENDENTE", "Pendente"),
            ("RESPONDIDA", "Respondida")
        ],
        default="PENDENTE"
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.aluno.nome


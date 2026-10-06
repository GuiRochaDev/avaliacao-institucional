from django.shortcuts import render
from .models import avaliacao


def listar_avaliacao(request):
    avaliacoes = avaliacao.objects.all()
    return render(request, "avaliacao/lista.html", {
        "avaliacao": avaliacoes
    })


def criar_avaliacao(request):
    if request.method == "POST":
        avaliacao.objects.create(
            nota=request.POST.get("nota"),
            comentario=request.POST.get("comentario"),
            aluno_id=request.POST.get("aluno"),
            disciplina_id=request.POST.get("disciplina")
        )

    return render(request, "avaliacao/criar.html")


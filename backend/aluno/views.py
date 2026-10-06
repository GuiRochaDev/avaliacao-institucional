from django.http import JsonResponse
from .models import aluno

def listar_aluno(request):
    usuarios = aluno.objects.all().values('id','nome','ra', 'email', 'curso')
    return JsonResponse(list(aluno), safe=False)

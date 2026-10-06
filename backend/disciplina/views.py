from django.http import JsonResponse
from .models import disciplina

def listar_disciplina(request): 
    usuarios = disciplina.objects.all().values('id','nome', 'codigo', 'professor', 'periodo')
    return JsonResponse(list(disciplina), safe=False)    
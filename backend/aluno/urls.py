from django.urls import path
from .views import listar_aluno
urlpatterns = [path('aluno/', listar_aluno),]
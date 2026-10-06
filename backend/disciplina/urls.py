from django.urls import path
from .views import listar_disciplina
urlpatterns = [path('disciplina/', listar_disciplina),]
from django.urls import path
from .views import listar_avaliacao
from .views import criar_avaliacao
urlpatterns = [
path('avaliacao/', listar_avaliacao),
path('avaliacao/', criar_avaliacao),
]
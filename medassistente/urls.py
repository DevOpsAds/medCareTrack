from django.urls import path
from . import views


urlpatterns = [
    # Define a URL para criar um novo cuidador
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/salvar_recurso/', views.salvar_recurso, name='salvar_recurso'),
 
]

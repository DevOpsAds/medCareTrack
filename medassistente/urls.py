from django.urls import path
from .views import cadastro


urlpatterns = [
    # Define a URL para criar um novo cuidador
    path('cadastro/', cadastro, name='cadastro'),
 
]

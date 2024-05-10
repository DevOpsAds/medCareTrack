from django.contrib.auth import get_user_model

from django.db import models
from accounts.models import UsuarioVinculado



class OpcoesContato(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    TIPO_CONTATO_CHOICES = [
        ('Telefone', 'Telefone'),
        ('Rede_Social', 'Rede Social'),
        ('Outro', 'Outro'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_CONTATO_CHOICES)
    numero_identificador = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo}: {self.numero_identificador}"

class AgendaDisponivel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return f"{self.data_inicio} - {self.data_fim}"

class RecursoDisponivel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    TIPO_RECURSO_CHOICES = [
        ('Financeiro', 'Financeiro'),
        ('Locomoção', 'Locomoção'),
        ('Alimentação', 'Alimentação'),
        ('Outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_RECURSO_CHOICES)

    def __str__(self):
        return f"{self.nome} - {self.tipo}"
    

class Cuidador(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE)
    idade = models.PositiveIntegerField()
    contatos = models.ManyToManyField(OpcoesContato, related_name='opcoes_contato')
    agenda_disponibilidade = models.ManyToManyField(AgendaDisponivel, related_name='cuidadores')

    def __str__(self):
        return self.nome.nome.nome  # Obtendo o nome do usuário vinculado



class UsuarioCuidador(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)  # Campo para armazenar a senha

    def __str__(self):
        return f"{self.usuario.username} - {self.cuidador.nome}"
from django.contrib.auth.models import User
from django.db import models

class Cuidador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    contatos = models.ManyToManyField('OpcoesContato')
    agenda_disponibilidade = models.ManyToManyField('AgendaDisponivel', related_name='cuidadores')

    def __str__(self):
        return self.nome

class OpcoesContato(models.Model):
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
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()

    def __str__(self):
        return f"{self.data_inicio} - {self.data_fim}"

class RecursoDisponivel(models.Model):
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

class UsuarioCuidador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cuidador = models.ForeignKey(Cuidador, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)  # Campo para armazenar a senha

    def __str__(self):
        return f"{self.usuario.username} - {self.cuidador.nome}"
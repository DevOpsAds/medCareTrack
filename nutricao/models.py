from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from accounts.models import UsuarioVinculado


# Classe comum
class Alimentacao(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    TIPO_ALIMENTO_CHOICES = [
        ('CA', 'Café da Manhã'),
        ('AL', 'Almoço'),
        ('JA', 'Jantar'),
        ('LA', 'Lanche'),
        ('OU', 'Outro'),
    ]

    tipo_alimento = models.CharField(max_length=2, choices=TIPO_ALIMENTO_CHOICES)
    descricao = models.TextField()
    hora_consumo = models.DateTimeField()
    calorias = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_tipo_alimento_display()}: {self.descricao} ({self.calorias} cal)"






# Classe comum
class Liquido(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    TIPO_LIQUIDO_CHOICES = [
        ('AG', 'Água'),
        ('SU', 'Suco'),
        ('RE', 'Refrigerante'),
        ('CH', 'Chá'),
        ('OU', 'Outro'),
    ]

    tipo_liquido = models.CharField(max_length=2, choices=TIPO_LIQUIDO_CHOICES)
    descricao = models.TextField()
    hora_consumo = models.DateTimeField()
    volume_ml = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo_liquido}: {self.descricao} ({self.volume_ml} ml)"




class EscalaQuantidade(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    VALORES_ESCALA = [
        (0, 'Ruim'),
        (1, 'Muito Ruim'),
        (2, 'Ruim'),
        (3, 'Abaixo do Esperado'),
        (4, 'Adequado'),
        (5, 'Bom'),
        (6, 'Bem'),
        (7, 'Muito Bem'),
        (8, 'Ótimo'),
        (9, 'Excelente'),
        (10, 'Ótimo'),
    ]

    valor = models.PositiveSmallIntegerField(choices=VALORES_ESCALA, default=5)

    def __str__(self):
        return f"{self.get_valor_display()} ({self.valor})"



class RegistroAlimentacao(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    horario = models.TimeField(default=timezone.now)
    alimentacao = models.ForeignKey(Alimentacao, on_delete=models.CASCADE)
    qualidade = models.ForeignKey(EscalaQuantidade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Registro de Alimentação de {self.user} em {self.horario}'

class RegistroLiquidos(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    horario = models.TimeField(default=timezone.now)
    liquido = models.ForeignKey(Liquido, on_delete=models.CASCADE)
    quantidade = models.ForeignKey(EscalaQuantidade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Registro de Líquidos de {self.user} em {self.horario}'
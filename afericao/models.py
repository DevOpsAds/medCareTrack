from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import UsuarioVinculado

class InstrumentoAfericao(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    informacoes = models.TextField()
    

    def __str__(self):
        return self.nome


class Aferitivos(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    instrumento = models.ForeignKey(InstrumentoAfericao, on_delete=models.CASCADE)
    nome_resultante = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_resultante


class ResultadosAferitivos(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    instrumento = models.ForeignKey(InstrumentoAfericao, on_delete=models.CASCADE)
    aferitivo = models.ForeignKey(Aferitivos, on_delete=models.CASCADE)  # Adicionando a chave estrangeira para Aferitivos
    resultados = models.FloatField(default=5.15)
    resultados_anteriores = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Resultado de {self.instrumento.nome}: {self.resultados}"
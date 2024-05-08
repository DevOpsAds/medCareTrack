from django.db import models
from django.contrib.auth import get_user_model


class TipoMedicamento(models.TextChoices):
    LIQUIDO = 'LI', 'Líquido'
    COMPRIMIDO = 'CO', 'Comprimido'
    ADESIVO = 'AD', 'Adesivo'
    INJETAVEL = 'IN', 'Injetável'

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=2, choices=TipoMedicamento.choices)

    def __str__(self):
        return self.nome

class MedicamentoExtendido(models.Model):
    medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE, primary_key=True)
    nome_fabricante = models.CharField(max_length=100)
    serventia = models.CharField(max_length=100)
    formulacao_basica = models.CharField(max_length=100)
    data_validade = models.DateField()
    ESTADO_CHOICES = (
        ('LI', 'Líquido'),
        ('SO', 'Sólido'),
        ('GA', 'Gasoso'),
    )
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    categoria = models.CharField(max_length=100)
    forma_farmaceutica = models.CharField(max_length=100)

    def __str__(self):
        return self.medicamento.nome

class Estoque(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='estoque')
    quantidade_atual = models.PositiveIntegerField(default=0)
    # Outros campos relevantes sobre o estoque
    
    def __str__(self):
        return f"{self.medicamento.nome} - {self.quantidade_atual} em estoque"
    



class MovimentoEstoque(models.Model):
    medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_movimento = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Movimentos de Estoque'

    def __str__(self):
        return f"{self.medicamento.nome} - {self.quantidade} unidades em {self.data_movimento}"


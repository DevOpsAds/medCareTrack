from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from accounts.models import UsuarioVinculado

class TipoMedicamento(models.TextChoices):
    LIQUIDO = 'LI', 'Líquido'
    COMPRIMIDO = 'CO', 'Comprimido'
    ADESIVO = 'AD', 'Adesivo'
    INJETAVEL = 'IN', 'Injetável'

class Medicamento(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=2, choices=TipoMedicamento.choices)

    def __str__(self):
        return self.nome

class MedicamentoExtendido(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cuidador = models.ForeignKey(UsuarioVinculado, on_delete=models.CASCADE, null=True, blank=True)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='estoque')
    quantidade_atual = models.PositiveIntegerField(default=0)
    # Outros campos relevantes sobre o estoque
    
    def __str__(self):
        return f"{self.medicamento.nome} - {self.quantidade_atual} em estoque"

    def adicionar_quantidade(self, quantidade):
        self.quantidade_atual += quantidade
        self.save()

    def remover_quantidade(self, quantidade):
        if quantidade <= self.quantidade_atual:
            self.quantidade_atual -= quantidade
            self.save()
        else:
            raise ValueError("Quantidade a ser removida excede a quantidade atual em estoque")




class MovimentoEstoque(models.Model):
   
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    OPERACAO_CHOICES = [
        ('AD', 'Adição'),
        ('RE', 'Remoção'),
    ]

    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    operacao = models.CharField(max_length=2, choices=OPERACAO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data_movimento = models.DateTimeField(auto_now_add=True)
    

    def salvar_movimento(self):
        if self.operacao == 'AD':
            Estoque.objects.filter(medicamento=self.medicamento).update(quantidade_atual=models.F('quantidade_atual') + self.quantidade)
        elif self.operacao == 'RE':
            estoque = Estoque.objects.get(medicamento=self.medicamento)
            if self.quantidade <= estoque.quantidade_atual:
                estoque.quantidade_atual -= self.quantidade
                estoque.save()
            else:
                raise ValueError("Quantidade a ser removida excede a quantidade atual em estoque")
        self.save()

    def __str__(self):
        return f"{self.get_operacao_display()} - {self.quantidade} de {self.medicamento.nome} em {self.data_movimento}"


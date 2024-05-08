from django import forms

class EntradaEstoqueForm(forms.Form):
    quantidade = forms.IntegerField(label='Quantidade de entrada', min_value=1)

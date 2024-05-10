from django import forms
from django.contrib.auth import get_user_model
from .models import OpcoesContato, AgendaDisponivel, RecursoDisponivel, Cuidador

User = get_user_model()

class OpcoesContatoForm(forms.ModelForm):
    class Meta:
        model = OpcoesContato
        fields = ['tipo', 'numero_identificador']
        widgets = {
            'tipo': forms.Select(choices=OpcoesContato.TIPO_CONTATO_CHOICES),
        }

    def __init__(self, *args, **kwargs):
            user = kwargs.pop('user', None)  # Recebendo o usuário como argumento
            super().__init__(*args, **kwargs)
            if user:
                self.fields['user'].initial = user  # Definindo o valor inicial do campo user
                self.fields['user'].widget = forms.HiddenInput()  # Ocultando o campo user

class AgendaDisponivelForm(forms.ModelForm):
    class Meta:
        model = AgendaDisponivel
        fields = ['user', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()

class RecursoDisponivelForm(forms.ModelForm):
    class Meta:
        model = RecursoDisponivel
        fields = ['user', 'nome', 'tipo']
        widgets = {
            'tipo': forms.Select(choices=RecursoDisponivel.TIPO_RECURSO_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()

class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = ['nome', 'idade', 'contatos', 'agenda_disponibilidade']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
              self.fields['user'].widget = forms.HiddenInput()
        self.fields['contatos'].widget = forms.CheckboxInput(attrs={'id': 'modalBtn_contato'}) # não altere esse 
        self.fields['agenda_disponibilidade'].widget = forms.CheckboxInput(attrs={'id': 'myBtn_modal_agenda'}) # não altere esse 


 # self.fields['user'].queryset = User.objects.filter(pk=self.user.pk)


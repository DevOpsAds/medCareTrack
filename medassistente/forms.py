from django import forms
from django.contrib.auth.models import User
from .models import Cuidador,AgendaDisponivel,OpcoesContato,RecursoDisponivel,UsuarioCuidador




from django.contrib.auth.forms import AuthenticationForm

class CuidadorAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.usuario_cuidador.exists():
            raise forms.ValidationError(
                "Você não tem permissão para acessar esta área."
            )

#UsuarioCuidador

class UsuarioCuidadorForm(forms.ModelForm):
    class Meta:
        model = UsuarioCuidador
        fields = ['usuario', 'cuidador', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),  # Campo de senha para entrada oculta
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Defina o campo 'usuario' como um campo de seleção dropdown com os usuários existentes
        self.fields['usuario'].queryset = User.objects.all()


class RecursoDisponivelForm(forms.ModelForm):
    class Meta:
        model = RecursoDisponivel
        fields = ['nome', 'tipo']

    def __init__(self, *args, **kwargs):
        super(RecursoDisponivelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control'})


class AgendaDisponivelForm(forms.ModelForm):
    class Meta:
        model = AgendaDisponivel
        fields = ['data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = ['nome', 'idade', 'contatos', 'agenda_disponibilidade']

    def __init__(self, *args, **kwargs):
        super(CuidadorForm, self).__init__(*args, **kwargs)
        self.fields['contatos'].widget = forms.CheckboxInput(attrs={'id': 'modalBtn_contato'})
        self.fields['agenda_disponibilidade'].widget = forms.CheckboxInput(attrs={'id': 'myBtn_modal_agenda'})



class OpcoesContatoForm(forms.ModelForm):
    class Meta:
        model = OpcoesContato
        fields = ['tipo', 'numero_identificador']

    def __init__(self, *args, **kwargs):
        super(OpcoesContatoForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero_identificador'].widget.attrs.update({'class': 'form-control'})

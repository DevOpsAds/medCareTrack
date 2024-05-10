from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User  # Importe o modelo de usuário do Django
from .models import UsuarioVinculado

class UsuarioVinculadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UsuarioVinculadoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')

        if senha:
            if len(senha) < 8:
                self.add_error('senha', "A senha deve conter pelo menos 8 caracteres.")
            if not any(char.isupper() for char in senha):
                self.add_error('senha', "A senha deve conter pelo menos uma letra maiúscula.")
            if not any(char.islower() for char in senha):
                self.add_error('senha', "A senha deve conter pelo menos uma letra minúscula.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        senha = self.cleaned_data.get('senha')
        
        if senha:
            instance.senha_hash = make_password(senha)
            instance.senha = ""  # Limpa a senha em texto puro

        if self.user: 
            if isinstance(self.user, User):  # Verifica se o usuário é uma instância de User
                instance.usuario_principal_id = self.user  # Define o usuário principal como o usuário logado
            else:
                raise ValueError("O usuário passado não é uma instância de User.")

        if commit:
            instance.save()
        return instance

    class Meta:
        model = UsuarioVinculado
        fields = ['nome', 'email', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),  # Definindo o widget para o campo senha
        }

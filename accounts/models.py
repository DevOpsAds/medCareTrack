from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import re


class UsuarioVinculado(models.Model):
    usuario_principal_id = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=128)  # Campo para receber a senha em texto puro
    senha_hash = models.CharField(max_length=128)  # Armazena o hash da senha

    def clean(self):
        # Valida a senha antes de salvar
        if self.senha:
            if len(self.senha) < 8:
                raise ValidationError("A senha deve conter pelo menos 8 caracteres.")
            if not re.search(r'[A-Z]', self.senha):
                raise ValidationError("A senha deve conter pelo menos uma letra maiúscula.")
            if not re.search(r'[a-z]', self.senha):
                raise ValidationError("A senha deve conter pelo menos uma letra minúscula.")

    def save(self, *args, **kwargs):
        # Ao salvar, criptografa a senha e armazena o hash
        if self.senha:
            self.senha_hash = make_password(self.senha)
            self.senha = ""  # Limpa a senha em texto puro
        super().save(*args, **kwargs)

    def verificar_senha(self, senha):
        # Verifica se a senha fornecida corresponde à senha armazenada
        return check_password(senha, self.senha_hash)

    def __str__(self):
        return self.nome


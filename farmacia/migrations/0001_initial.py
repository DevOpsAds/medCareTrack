# Generated by Django 5.0.4 on 2024-05-06 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('LI', 'Líquido'), ('CO', 'Comprimido'), ('AD', 'Adesivo'), ('IN', 'Injetável')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='MedicamentoExtendido',
            fields=[
                ('medicamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='farmacia.medicamento')),
                ('nome_fabricante', models.CharField(max_length=100)),
                ('serventia', models.CharField(max_length=100)),
                ('formulacao_basica', models.CharField(max_length=100)),
                ('data_validade', models.DateField()),
                ('estado', models.CharField(choices=[('LI', 'Líquido'), ('SO', 'Sólido'), ('GA', 'Gasoso')], max_length=2)),
                ('categoria', models.CharField(max_length=100)),
                ('forma_farmaceutica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_atual', models.PositiveIntegerField(default=0)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoque', to='farmacia.medicamento')),
            ],
        ),
    ]
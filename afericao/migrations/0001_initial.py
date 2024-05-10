# Generated by Django 5.0.4 on 2024-05-10 13:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentoAfericao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('informacoes', models.TextField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadosAferitivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultados', models.FloatField(default=5.15)),
                ('instrumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afericao.instrumentoafericao')),
                ('resultados_anteriores', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='afericao.resultadosaferitivos')),
            ],
        ),
    ]

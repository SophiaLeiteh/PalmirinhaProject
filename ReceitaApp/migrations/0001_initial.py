# Generated by Django 5.0.3 on 2024-04-02 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ingredientes', models.TextField(max_length=2000)),
                ('modo_de_preparo', models.TextField(max_length=8000)),
                ('grau_de_dificuladade', models.CharField(max_length=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReceitaApp.categoria')),
            ],
        ),
    ]

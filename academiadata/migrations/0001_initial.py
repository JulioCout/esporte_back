# Generated by Django 5.0 on 2024-09-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
        ),
    ]

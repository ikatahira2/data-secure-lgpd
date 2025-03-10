# Generated by Django 5.0.7 on 2024-07-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DadosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('consentimento', models.BooleanField(default=False)),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

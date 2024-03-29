# Generated by Django 2.2.1 on 2019-06-11 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rua', models.CharField(blank=True, max_length=240, null=True)),
                ('bairro', models.CharField(blank=True, max_length=240, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('cidade', models.CharField(blank=True, max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conjugues',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=240)),
                ('cpf', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('data_nascimento', models.DateField()),
                ('cedula_indentificacao', models.CharField(blank=True, max_length=9, null=True)),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('orgao_expedidor', models.CharField(blank=True, max_length=240, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('celular', models.CharField(blank=True, max_length=14, null=True)),
                ('n_carteira_trabalho', models.CharField(blank=True, max_length=12, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=240, null=True)),
                ('empresa', models.IntegerField(blank=True, null=True)),
                ('data_admissao', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=240)),
                ('cnpj', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.CharField(blank=True, max_length=240, null=True)),
                ('cidade', models.CharField(blank=True, max_length=240, null=True)),
                ('bairro', models.CharField(blank=True, max_length=240, null=True)),
                ('rua', models.CharField(blank=True, max_length=240, null=True)),
                ('numero', models.CharField(blank=True, max_length=5, null=True)),
                ('complemento', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('evento', models.CharField(max_length=240)),
                ('data', models.DateField()),
                ('status', models.BooleanField()),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrauEscolaridade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('escolaridade', models.CharField(blank=True, max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEstadoCivil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ufs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=240)),
                ('cpf', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('cedula_indentificacao', models.CharField(blank=True, max_length=9, null=True)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
                ('celular', models.CharField(blank=True, max_length=14, null=True)),
                ('data_emissao', models.DateField(blank=True, null=True)),
                ('orgao_expedidor', models.CharField(blank=True, max_length=240, null=True)),
                ('n_carteira_trabalho', models.CharField(blank=True, max_length=12, null=True)),
                ('nacionalidade', models.CharField(blank=True, max_length=240, null=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('tempo_no_brasil', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=240, null=True)),
                ('reg_casamento', models.CharField(blank=True, max_length=240, null=True)),
                ('nome_pai', models.CharField(blank=True, max_length=240, null=True)),
                ('naturalidade_pai', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=240, null=True)),
                ('naturalidade_mae', models.CharField(blank=True, max_length=100, null=True)),
                ('profissao', models.CharField(blank=True, max_length=240, null=True)),
                ('data_admissao', models.DateField(blank=True, null=True)),
                ('cedula_identificacao_conjuge', models.CharField(blank=True, max_length=20, null=True)),
                ('cep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Cep')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Empresa')),
                ('escolaridade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.GrauEscolaridade')),
                ('estado_civil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.TipoEstadoCivil')),
                ('nome_conjuge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Conjugues')),
                ('tipo_moradia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.TipoImovel')),
                ('uf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Ufs')),
            ],
        ),
        migrations.CreateModel(
            name='FequenciaEvento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Evento')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='uf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Ufs'),
        ),
        migrations.CreateModel(
            name='Dependentes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=240)),
                ('data_nascimento', models.DateField(null=True)),
                ('cpf', models.CharField(blank=True, max_length=9, null=True)),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='conjugues',
            name='escolaridade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gestao.GrauEscolaridade'),
        ),
    ]

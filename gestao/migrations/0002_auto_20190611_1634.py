# Generated by Django 2.2.1 on 2019-06-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conjugues',
            name='trabalha',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='trabalha',
            field=models.BooleanField(default=False),
        ),
    ]

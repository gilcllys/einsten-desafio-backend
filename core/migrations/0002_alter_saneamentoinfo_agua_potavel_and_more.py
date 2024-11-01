# Generated by Django 5.1.2 on 2024-11-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saneamentoinfo',
            name='agua_potavel',
            field=models.BooleanField(db_column='agua_potavel', default=False),
        ),
        migrations.AlterField(
            model_name='saneamentoinfo',
            name='coleta_lixo',
            field=models.BooleanField(db_column='coleta_lixo', default=False),
        ),
        migrations.AlterField(
            model_name='saneamentoinfo',
            name='instalacoes_sanitarias',
            field=models.BooleanField(db_column='instalacoes_sanitarias', default=False),
        ),
    ]
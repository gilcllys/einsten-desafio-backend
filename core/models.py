from django.db import models


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Paciente(ModelBase):
    class GenerosChoices(models.TextChoices):
        MC = "MC", "Mulher cisgênero"
        MTG = "MTG", "Mulher transgênero"
        HC = "HC", "Homem cisgênero"
        HTG = "HTG" "Homem transgênero"
        GNB = "GNB",  "Gênero não-binário"
        A = "A", "Agênero"
        GF = "GF", "Gênero-fluido"
        B = "B", "Bigênero"
        MTS = "MTS", "Mulher transexual"
        HTS = "HTS", "Homem transexual"
        P = "P", "Poligênero"
        O = "O", "Outros"
        ND = "ND", "Não declarado"
    nome = models.CharField(
        db_index=False,
        max_length=128,
        null=False,
        blank=False,
        db_column='nome',
    )
    genero = models.CharField(
        db_index=False,
        max_length=20,
        choices=GenerosChoices,
        default=GenerosChoices.ND,
        null=False,
        blank=False,
        db_column='genero',
    )
    has_esgoto = models.BooleanField(
        db_index=False,
        null=False,
        default=False,
        db_column='has_esgoto',
    )
    historico_saude = models.TextField(
        db_index=False,
        null=False,
        blank=False,
        db_column='historico_saude',
    )

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class SaneamentoInfo(ModelBase):

    bairro = models.CharField(
        db_index=False,
        max_length=30,
        null=False,
        blank=False,
        db_column='Bairro',
    )
    cidade = models.CharField(
        db_index=False,
        max_length=30,
        null=False,
        blank=False,
        db_column='cidade',
    )
    agua_potavel = models.BooleanField(
        db_index=False,
        null=False,
        default=False,
        db_column='agua_potavel',
    )
    coleta_lixo = models.BooleanField(
        db_index=False,
        null=False,
        default=False,
        db_column='coleta_lixo',
    )
    instalacoes_sanitarias = models.BooleanField(
        db_index=False,
        null=False,
        default=False,
        db_column='instalacoes_sanitarias',
    )

    class Meta:
        verbose_name = "SaneamentoInfo"
        verbose_name_plural = "SaneamentoInfos"

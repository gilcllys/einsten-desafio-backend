from rest_framework import serializers
from django.contrib.auth.models import User
from core import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paciente
        fields = '__all__'


class SaneamentoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SaneamentoInfo
        fields = '__all__'

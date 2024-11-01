from rest_framework.decorators import action
from urllib import response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from core import serializer, custom_serializer, behavior
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from core import models
from rest_framework.response import Response
from rest_framework import status


class RegisterView(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = custom_serializer.RegisterCustomSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.RegisterBehavior(data=data_serializer).run()
        return response


class LoginView(TokenObtainPairView):

    def get(self, request):
        data = request.data
        serializer = custom_serializer.LoginCustomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.LoginBehavior(data=data_serializer).run()
        return response


class LogoutView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = custom_serializer.RegisterCustomSerializer

    def post(self, request):
        data = request.data
        serializer = custom_serializer.LogoutCustomSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = behavior.LogoutBehavior(data=data_serializer).run()
        return response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserSerializer
    queryset = User.objects.all()


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.PacienteSerializer
    queryset = models.Paciente.objects.all()

    @action(detail=False, methods=['post'])
    def filtrar(self, request):
        # Obtém os parâmetros do payload JSON
        nome = request.data.get('nome')
        genero = request.data.get('genero')
        has_esgoto = request.data.get('has_esgoto')

        # Inicializa o QuerySet com todos os objetos do modelo Produto
        queryset = models.Paciente.objects.all()

        # Filtra os produtos com base nos parâmetros fornecidos no payload
        if nome:
            queryset = queryset.filter(nome=nome)
        if genero:
            queryset = queryset.filter(genero=genero)
        if has_esgoto:

            queryset = queryset.filter(
                has_esgoto=has_esgoto)

        # Serializa os dados filtrados e retorna a resposta
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SaneamentoInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.SaneamentoInfoSerializer
    queryset = models.SaneamentoInfo.objects.all()

    @action(detail=False, methods=['post'])
    def filtrar(self, request):
        # Obtém os parâmetros do payload JSON
        bairro = request.data.get('bairro')
        cidade = request.data.get('cidade')
        agua_potavel = request.data.get('agua_potavel')
        coleta_lixo = request.data.get('coleta_lixo')
        instalacoes_sanitarias = request.data.get('instalacoes_sanitarias')

        # Inicializa o QuerySet com todos os objetos do modelo Produto
        queryset = models.SaneamentoInfo.objects.all()

        # Filtra os produtos com base nos parâmetros fornecidos no payload
        if bairro:
            queryset = queryset.filter(bairro=bairro)
        if cidade:
            queryset = queryset.filter(cidade=cidade)
        if agua_potavel:
            queryset = queryset.filter(
                agua_potavel=agua_potavel)
        if coleta_lixo:
            queryset = queryset.filter(
                agua_potavel=coleta_lixo)
        if instalacoes_sanitarias:
            queryset = queryset.filter(
                agua_potavel=instalacoes_sanitarias)

        # Serializa os dados filtrados e retorna a resposta
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

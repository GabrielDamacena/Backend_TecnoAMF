from rest_framework import serializers
from .models import Usuario, Semestre

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'nome','cpf', 'matricula', 'data_nascimento', 'semestre']

class SemestreSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Semestre
        fields = ['id', 'usuario', 'semestre', 'dia_semana', 'cadeira']

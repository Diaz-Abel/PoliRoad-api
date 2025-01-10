from rest_framework import serializers
from .models import Carrera, Materia, Facultad


class MallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = "__all__"


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = "__all__"

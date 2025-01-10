from rest_framework import viewsets

from .serializer import MallaSerializer, MateriaSerializer, FacultadSerializer

from .models import Carrera, Materia, Facultad

# Create your views here.


class CarreraView(viewsets.ModelViewSet):
    serializer_class = MallaSerializer
    queryset = Carrera.objects.all()

    def get_queryset(self):
        facultad_id = self.request.query_params.get("facultad", None)
        if facultad_id is not None:
            return self.queryset.filter(
                facultad__id=facultad_id
            )  # Filtrar por facultad
        return self.queryset  # Si no se pasa el parámetro, devuelve todas las carreras


class MateriaView(viewsets.ModelViewSet):
    serializer_class = MateriaSerializer
    queryset = Materia.objects.all()

    def get_queryset(self):
        carrera_id = self.request.query_params.get("carrera", None)
        if carrera_id is not None:
            return self.queryset.filter(
                plan_estudio__id=carrera_id
            )  # Filtrar por carrera
        return self.queryset  # Si no se pasa el parámetro, devuelve todas las cmaterias


class FacultadView(viewsets.ModelViewSet):
    serializer_class = FacultadSerializer
    queryset = Facultad.objects.all()

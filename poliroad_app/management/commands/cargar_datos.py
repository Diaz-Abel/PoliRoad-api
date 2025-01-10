import json
from django.core.management.base import BaseCommand
from poliroad_app.models import Facultad, Carrera, Materia


class Command(BaseCommand):
    help = "Carga datos de un archivo JSON en la base de datos"

    def handle(self, *args, **kwargs):
        # Ruta al archivo JSON
        json_path = "data/datos.json"

        with open(json_path, "r") as file:
            data = json.load(file)

        # Cargar facultades
        for facultad_data in data["facultades"]:
            facultad, created = Facultad.objects.get_or_create(
                id=facultad_data["id"], nombre=facultad_data["nombre"]
            )
            if created:
                self.stdout.write(f"Facultad creada: {facultad.nombre}")

        # Cargar carreras
        for carrera_data in data["carreras"]:
            facultad = Facultad.objects.get(id=carrera_data["facultad"])
            carrera, created = Carrera.objects.get_or_create(
                id=carrera_data["id"], nombre=carrera_data["nombre"], facultad=facultad
            )
            if created:
                self.stdout.write(f"Carrera creada: {carrera.nombre}")

        # Cargar materias
        for materia_data in data["materias"]:
            plan_estudio = Carrera.objects.get(id=materia_data["plan_estudio"])
            materia, created = Materia.objects.get_or_create(
                id=materia_data["id"],
                nombre=materia_data["nombre"],
                semestre=materia_data["semestre"],
                plan_estudio=plan_estudio,
            )
            for dep_id in materia_data["dependencias"]:
                dependencia = Materia.objects.get(id=dep_id)
                materia.dependencias.add(dependencia)

            materia.save()
            if created:
                self.stdout.write(f"Asignatura creada: {materia.nombre}")

        self.stdout.write(self.style.SUCCESS("Datos cargados correctamente."))

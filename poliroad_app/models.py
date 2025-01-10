from django.db import models


class Facultad(models.Model):
    nombre = models.CharField(max_length=100, default="FP-UNA San Lorenzo")

    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    facultad = models.ForeignKey(
        Facultad, related_name="mallas", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    SEMESTRE_CHOICES = [
        (i, f"Semestre {i}") for i in range(1, 11)  # Genera las opciones de 1 a 10
    ]

    nombre = models.CharField(max_length=100)
    # dependencias con otras materias
    plan_estudio = models.ForeignKey(
        Carrera, related_name="materias", on_delete=models.CASCADE
    )
    dependencias = models.ManyToManyField("self", symmetrical=False, blank=True)

    semestre = models.IntegerField(choices=SEMESTRE_CHOICES)

    def __str__(self):
        return self.nombre

from django.contrib import admin

from .models import Carrera, Materia, Facultad

# Register your models here.
admin.site.register(Carrera)

admin.site.register(Facultad)


class MateriaAdmin(admin.ModelAdmin):
    # Mostrar una vista de checkbox múltiple para la relación ManyToMany
    filter_horizontal = ("dependencias",)


admin.site.register(Materia, MateriaAdmin)

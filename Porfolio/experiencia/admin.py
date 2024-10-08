from django.contrib import admin
from .models import Experiencia

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['curso','institucion_del_curso', 'fecha_curso', 'numero_horas']
    search_fields = ['curso','institucion_del_curso', 'descripcion_curso']

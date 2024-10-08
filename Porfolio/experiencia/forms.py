from django import forms
from .models import Experiencia

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['curso','institucion_del_curso', 'descripcion_curso', 'fecha_curso', 'numero_horas']

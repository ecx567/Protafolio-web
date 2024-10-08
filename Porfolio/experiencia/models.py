from django.db import models

class Experiencia(models.Model):
    curso = models.CharField(max_length=255, blank=True, null=True)
    institucion_del_curso = models.CharField(max_length=255)
    descripcion_curso = models.TextField()
    fecha_curso = models.DateField()
    numero_horas = models.IntegerField()

    def __str__(self):
        return f"{self.curso} - {self.institucion_del_curso} - {self.descripcion_curso}"

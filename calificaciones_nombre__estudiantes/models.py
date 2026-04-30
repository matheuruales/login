from django.db import models
from django.db.models import Avg


class Calificacion(models.Model):
    nombre_estudiante = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    asignatura = models.CharField(max_length=100)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2)
    promedio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        editable=False,
        default=0,
    )

    def __str__(self) -> str:
        return f"{self.nombre_estudiante} - {self.asignatura}"

    def calcular_promedio(self):
        return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

    def save(self, *args, **kwargs):
        self.promedio = self.calcular_promedio()
        return super().save(*args, **kwargs)

    @classmethod
    def obtener_promedio_general(cls):
        return cls.objects.aggregate(promedio_general=Avg("promedio"))["promedio_general"]
